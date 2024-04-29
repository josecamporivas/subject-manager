import flask_login
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(flask_login.UserMixin):
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

    def get_id(self):
        return self.username

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'username': self.username
        }