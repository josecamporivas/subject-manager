from werkzeug.security import generate_password_hash, check_password_hash

class Student():
    def __init__(self, full_name, username, password, subjects: list):
        self.__full_name = full_name
        self.__username = username
        self.__password = generate_password_hash(password)
        self.__subjects = subjects

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
    def subjects(self):
        return self.__subjects

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name

    @username.setter
    def username(self, username):
        self.__username = username

    @password.setter
    def password(self, password):
        self.__password = generate_password_hash(password)

    @subjects.setter
    def subjects(self, subjects):
        self.__subjects = subjects

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add_subject(self, subject):
        try:
            self.__subjects.remove(subject)
        except ValueError:
            pass
        self.__subjects.append(subject)

    def remove_subject(self, subject):
        try:
            self.__subjects.remove(subject)
        except ValueError:
            pass

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'username': self.username,
            'subjects': self.subjects
        }


