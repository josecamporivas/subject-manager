import flask
import sirope
import flask_login
from dotenv import load_dotenv
from os import getenv

from blueprints.subject_bp import subject_bp
from blueprints.teacher_bp import teacher_bp
from models.Teacher import Teacher

load_dotenv()

def create_app():
    login_manager = flask_login.login_manager.LoginManager()
    flask_app = flask.Flask(__name__)
    sirope_inst = sirope.Sirope()

    flask_app.config['SECRET_KEY'] = getenv('SECRET_KEY_FLASK')
    login_manager.init_app(flask_app)
    return flask_app, sirope_inst, login_manager

app, srp, lm = create_app()
app.register_blueprint(teacher_bp)
app.register_blueprint(subject_bp)

@lm.user_loader
def load_user(id: str):
    print(f'Loading user {id}')
    return srp.find_first(Teacher, lambda x: x.username == id)

@lm.unauthorized_handler
def unauthorized():
    print('Unauthorized')
    flask.flash("Unauthorized")
    return flask.redirect('/')

@app.route('/')
def index():
    return flask.render_template('login/index.html')

@app.route('/login', methods=['POST'])
def login():
    username = flask.request.form['username']
    password = flask.request.form['password']
    user = srp.find_first(Teacher, lambda x: x.username == username)

    if not user:
        return {'error': 'User not found'}, 404

    if not user.check_password(password):
        return {'error': 'Invalid password'}, 401

    flask_login.login_user(user)
    return {'message': 'Logged in'}, 200

if __name__ == '__main__':
    app.run()
