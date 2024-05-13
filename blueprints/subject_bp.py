import json

from flask import Blueprint, render_template, request
from sirope import Sirope

from models.Student import Student
from models.Subject import Subject
from models.Teacher import Teacher
from utils.input_validators import check_empty_string

subject_bp = Blueprint('subject_bp', __name__, url_prefix='/subjects', template_folder='templates')
srp = Sirope()

@subject_bp.route('/')
def index():
    data = {
        'subjects': srp.load_all(Subject)
    }

    return render_template('subject/index.html', **data)

@subject_bp.route('/', methods=['POST'])
def create():
    data = json.loads(request.data.decode('utf-8'))
    valid_inputs = check_empty_string(data.get('name')) and check_empty_string(data.get('classroom'))
    if not valid_inputs:
        return {'message': 'Empty fields'}, 400

    exists = srp.find_first(Subject, lambda x: x.name == data.get('name'))
    if exists:
        return {'message': 'Subject already exists'}, 409

    subject = Subject(**data)
    srp.save(subject)

    return subject.to_dict(), 201

@subject_bp.route('/<name>', methods=['PUT'])
def update(name):
    subject = srp.find_first(Subject, lambda x: x.name == name)
    if not subject:
        return {'message': 'Subject not found'}, 404

    data = json.loads(request.data.decode('utf-8'))
    valid_inputs = check_empty_string(data.get('classroom'))
    if not valid_inputs:
        return {'message': 'Empty fields'}, 400

    subject.classroom = data.get('classroom')
    srp.save(subject)

    return subject.to_dict(), 200

@subject_bp.route('/<name>', methods=['DELETE'])
def delete(name):
    subject = srp.find_first(Subject, lambda x: x.name == name)
    if not subject:
        return {'message': 'Subject not found'}, 404

    students = srp.load_all(Student)
    for student in students:
        if name in student.subjects:
            try:
                student.subjects.remove(name)
                srp.save(student)
            except ValueError:
                pass

    teachers = srp.load_all(Teacher)
    for teacher in teachers:
        if name == teacher.subject:
            teacher.subject = "<No subject>"
            srp.save(teacher)


    srp.delete(subject.__oid__)
    return {'message': 'Subject deleted'}, 204