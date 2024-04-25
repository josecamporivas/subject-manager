import flask
import flask_login
from flask import Blueprint
from sirope import Sirope

from models.Subject import Subject
from models.Teacher import Teacher
import json

from utils.auth import get_current_user
from utils.input_validators import check_empty_string

teacher_bp = Blueprint('teacher_bp', __name__, url_prefix='/teachers', template_folder='templates')
srp = Sirope()


@teacher_bp.route('/')
@flask_login.login_required
def index():
    get_current_user()

    data = {
        'teachers': list(srp.load_all(Teacher)),
        'subjects': list(srp.load_all(Subject))
    }

    return flask.render_template('teacher/index.html', **data)


@teacher_bp.route('/', methods=['POST'])
def create():
    data = json.loads(flask.request.data.decode('utf-8'))
    full_name, username, password, subject = data.get('full_name'), data.get('username'), data.get('password'), data.get('subject')
    valid_inputs = (check_empty_string(full_name) and check_empty_string(username)
                    and check_empty_string(password)) and check_empty_string(subject)
    if not valid_inputs:
        return {'message': 'Empty fields'}, 400

    exists = srp.find_first(Teacher, lambda x: x.username == username)
    if exists:
        return {'message': 'Teacher already exists'}, 409

    teacher = Teacher(**data)
    srp.save(teacher)

    return teacher.to_dict(), 201


@teacher_bp.route('/<username>', methods=['PUT'])
def update(username):
    teacher_db = srp.find_first(Teacher, lambda x: x.username == username)
    if not teacher_db:
        return {'message': 'Teacher not found'}, 404

    data = json.loads(flask.request.data.decode('utf-8'))
    full_name, password, subject = data.get('full_name'), data.get('password'), data.get('subject')
    valid_inputs = check_empty_string(full_name) and check_empty_string(subject)
    if not valid_inputs:
        return {'message': 'Empty fields'}, 400

    teacher_db.full_name = full_name
    if not check_empty_string(password):
        teacher_db.password = password

    teacher_db.subject = subject
    srp.save(teacher_db)

    return teacher_db.to_dict(), 200

@teacher_bp.route('/<username>', methods=['DELETE'])
def delete(username):
    teacher_db = srp.find_first(Teacher, lambda x: x.username == username)
    if not teacher_db:
        return {'message': 'Teacher not found'}, 404

    isDeleted = srp.delete(teacher_db.__oid__)
    if not isDeleted:
        return {'message': 'Error deleting teacher'}, 500

    return {'message': 'Teacher deleted'}, 200


# @app.route('/saludo', methods=['POST'])
# def saludo():
#     # nombre = flask.request.form.get('name')
#     email = flask.request.form.get('email', "").strip()
#     password = flask.request.form.get('password', "").strip()
#     mensaje = flask.request.form.get('mensaje')
#
#     # if not nombre:
#     #     nombre = "Anónimo"
#
#     usr = User.find(srp, email)
#
#     if usr:
#         if not usr.compara_password(password):
#             flask.flash("usuario no reconocido")
#             return flask.redirect('/')
#     else:
#         usr = User(email, password)
#         srp.save(usr)
#
#     flask_login.login_user(usr)
#
#     if not mensaje:
#         mensaje = "Mensaje vacío"
#
#     data = Mensaje(usr.email, mensaje)
#     srp.save(data)
#
#     flask_login.logout_user()
#     return flask.redirect('/')