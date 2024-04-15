import flask_login
from werkzeug.security import generate_password_hash, check_password_hash
from sirope import Sirope

class Teacher(flask_login.UserMixin):
    def __init__(self, full_name, username, password):
        self.__full_name = full_name
        self.__username = username
        self.__password = generate_password_hash(password)

    @property
    def full_name(self):
        return self.__full_name

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def current_user():
        usr = flask_login.current_user

        if usr.is_anonymous:
            usr.logout_user()
            usr = None
        return usr

    @staticmethod
    def get(username, sirope_inst):
        return sirope_inst.get_teacher(username)

    @staticmethod
    def find(sirope_inst: Sirope, username):
        return sirope_inst.find_first(Teacher, lambda x: x.username == username)