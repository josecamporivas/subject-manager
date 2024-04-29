import flask
import flask_login
from flask import Blueprint
from sirope import Sirope

from models.Student import Student
from models.Subject import Subject

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
