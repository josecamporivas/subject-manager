import flask
import flask_login
from flask import Blueprint
from sirope import Sirope

from models.Admin import Admin
from utils.input_validators import check_empty_string

root_bp = Blueprint('root_bp', __name__, url_prefix='/', template_folder='templates')
srp = Sirope()

@root_bp.route('/')
def index():
    return flask.render_template('login/index.html')

@root_bp.route('/login', methods=['POST'])
def login():
    username = flask.request.form['username']
    password = flask.request.form['password']
    user = srp.find_first(Admin, lambda x: x.username == username)

    if not user:
        return {'message': 'Admin not found'}, 404

    if not user.check_password(password):
        return {'message': 'Invalid password'}, 401

    flask_login.login_user(user)
    return {'message': 'Logged in'}, 200

@root_bp.route('/logout', methods=['POST'])
def logout():
    flask_login.logout_user()
    return {'message': 'Logged out'}, 200

@root_bp.route('/register')
def register_page():
    return flask.render_template('login/register.html')

@root_bp.route('/register', methods=['POST'])
def register():
    data = flask.request.form
    full_name, username, password = data.get('full_name'), data.get('username'), data.get('password')
    valid_inputs = check_empty_string(full_name) and check_empty_string(username) and check_empty_string(password)
    if not valid_inputs:
        return {'message': 'Empty fields'}, 400

    exists = srp.find_first(Admin, lambda x: x.username == username)
    if exists:
        return {'message': 'Admin already exists'}, 409

    user = Admin(**data)
    srp.save(user)

    return user.to_dict(), 201

@root_bp.route('/dashboard')
@flask_login.login_required
def dashboard():
    return flask.render_template('dashboard/index.html')