import flask
from flask import Blueprint
from sirope import Sirope
from models.Teacher import Teacher

teacher_bp = Blueprint('teacher_bp', __name__, url_prefix='/teachers', template_folder='templates')
srp = Sirope()

@teacher_bp.route('/')
def index():
    data = {
        'teachers': srp.load_all(Teacher)
    }

    return flask.render_template('teacher/index.html', **data)
