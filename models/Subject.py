import flask_login

class Subject(flask_login.UserMixin):
    def __init__(self, name, classroom):
        self.__name = name
        self.__classroom = classroom

    @property
    def name(self):
        return self.__name

    @property
    def classroom(self):
        return self.__classroom

    @classroom.setter
    def classroom(self, classroom):
        self.__classroom = classroom

    def to_dict(self):
        return {
            'name': self.name,
            'classroom': self.classroom
        }
