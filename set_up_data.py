import sirope

from models.Admin import Admin
from models.Student import Student
from models.Teacher import Teacher
from models.Subject import Subject

srp = sirope.Sirope()

def create_teachers():
    teachers = [
        Teacher('Juan Carlos', 'juanca', 'juanca', 'Math'),
        Teacher('Antonio Recio', 'antoniorecio', 'password', 'Spanish'),
        Teacher('Marcial', 'marcial', 'password', 'Physical Education'),
        Teacher('Eugenio', 'eugenio', 'password', 'Music'),
        Teacher('Ramon', 'ramon', 'password', 'Science'),
        Teacher('Rafa Nadal', 'rafa', 'password', 'Physical Education')
    ]

    for teacher in teachers:
        srp.save(teacher)

def create_subjects():
    subjects = [
        Subject('Math', 'Laboratory 1'),
        Subject('Spanish', 'Laboratory 2'),
        Subject('Physical Education', 'Gym'),
        Subject('Music', 'Music Room'),
        Subject('Science', 'Laboratory 3'),
    ]

    for subject in subjects:
        srp.save(subject)

def create_students():
    students = [
        Student('Pedro', 'pedro', 'pedro', ['Math', 'Spanish']),
        Student('Juan', 'juan', 'juan', ['Physical Education', 'Music']),
        Student('Pablo', 'pablo', 'pablo', ['Science', 'Math'])
    ]

    for student in students:
        srp.save(student)

def create_admins():
    admins = [
        Admin('Administrator', 'admin', 'admin')
    ]

    for admin in admins:
        srp.save(admin)

if __name__ == '__main__':
    create_teachers()
    create_subjects()
    create_students()
    create_admins()
