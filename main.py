import flask
import sirope
import flask_login
from dotenv import load_dotenv
from os import getenv

from blueprints.root_bp import root_bp
from blueprints.student_bp import student_bp
from blueprints.subject_bp import subject_bp
from blueprints.teacher_bp import teacher_bp
from models.Admin import Admin

load_dotenv()

def create_app():
    login_manager = flask_login.login_manager.LoginManager()
    flask_app = flask.Flask(__name__)
    sirope_inst = sirope.Sirope()

    flask_app.config['SECRET_KEY'] = getenv('SECRET_KEY_FLASK')
    login_manager.init_app(flask_app)
    return flask_app, sirope_inst, login_manager

app, srp, lm = create_app()
app.register_blueprint(root_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(subject_bp)
app.register_blueprint(student_bp)

@lm.user_loader
def load_user(id: str):
    return srp.find_first(Admin, lambda x: x.username == id)

@lm.unauthorized_handler
def unauthorized():
    flask.flash("Unauthorized")
    return flask.redirect('/')

if __name__ == '__main__':
    app.run()
