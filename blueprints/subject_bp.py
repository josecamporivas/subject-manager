import json

from flask import Blueprint, render_template, request
from sirope import Sirope

from models.Subject import Subject
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

    subject = Subject(**data)
    srp.save(subject)

    return subject.to_dict(), 201
