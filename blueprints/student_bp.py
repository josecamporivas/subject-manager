import json

import flask
import flask_login
from flask import Blueprint
from sirope import Sirope

from models.Student import Student
from models.Subject import Subject
from utils.input_validators import check_empty_string, check_empty_list

student_bp = Blueprint('student_bp', __name__, url_prefix='/students', template_folder='templates')
srp = Sirope()


@student_bp.route('/')
@flask_login.login_required
def get_students():
    data = {
        'students': list(srp.load_all(Student)),
        'subjects': list(srp.load_all(Subject))
    }

    return flask.render_template('student/index.html', **data)


@student_bp.route('/', methods=['POST'])
def create_student():
    data = json.loads(flask.request.data.decode('utf-8'))
    full_name, username, password, subjects = data.get('full_name'), data.get('username'), data.get('password'), data.get('subjects')
    print(full_name, username, password, subjects)
    valid_inputs = check_empty_string(full_name) and check_empty_string(username) and check_empty_string(password) \
                   and check_empty_list(subjects)

    if not valid_inputs:
        return {'message': 'Empty fields'}, 400

    exists = srp.find_first(Student, lambda x: x.username == username)
    if exists:
        return {'message': 'Student username already exists'}, 409

    student = Student(full_name, username, password, subjects)
    srp.save(student)

    return student.to_dict(), 201

@student_bp.route('/<username>', methods=['PUT'])
def update_student(username):
    student = srp.find_first(Student, lambda x: x.username == username)
    if not student:
        return {'message': 'Student not found'}, 404

    data = json.loads(flask.request.data.decode('utf-8'))
    full_name, password, subjects = data.get('full_name'), data.get('password'), data.get('subjects')
    valid_inputs = check_empty_string(full_name) and check_empty_list(subjects)
    if not valid_inputs:
        return {'message': 'Empty fields'}, 400

    student.full_name = full_name
    if not check_empty_string(password):
        student.password = password
    student.subjects = subjects

    srp.save(student)

    return student.to_dict(), 200

@student_bp.route('/<username>', methods=['DELETE'])
def delete_student(username):
    student = srp.find_first(Student, lambda x: x.username == username)
    if not student:
        return {'message': 'Student not found'}, 404

    isDeleted = srp.delete(student.__oid__)
    if not isDeleted:
        return {'message': 'Error deleting student'}, 500

    return {'message': 'Student deleted'}, 200
