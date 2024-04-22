import flask_login
from werkzeug.security import generate_password_hash, check_password_hash

class Teacher(flask_login.UserMixin):
    def __init__(self, full_name, username, password, subject):
        self.__full_name = full_name
        self.__username = username
        self.__password = generate_password_hash(password)
        self.__subject = subject

    @property
    def full_name(self):
        return self.__full_name

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def subject(self):
        return self.__subject

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name

    @password.setter
    def password(self, password):
        self.__password = generate_password_hash(password)

    @subject.setter
    def subject(self, subject):
        self.__subject = subject

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'username': self.username,
            'subject': self.subject
        }
