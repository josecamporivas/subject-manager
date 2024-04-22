import sirope

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

if __name__ == '__main__':
    create_teachers()
    create_subjects()
