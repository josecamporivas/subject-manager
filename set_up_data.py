import sirope

from models.Teacher import Teacher

srp = sirope.Sirope()

def create_teachers():
    teachers = [
        Teacher('John Doe', 'john.doe', 'password'),
        Teacher('Jane Doe', 'jane.doe', 'password'),
        Teacher('John Smith', 'john.smith', 'password'),
        Teacher('Jane Smith', 'jane.smith', 'password'),
        Teacher('John Johnson', 'john.johnson', 'password'),
        Teacher('Jane Johnson', 'jane johnson', 'password')
    ]

    for teacher in teachers:
        srp.save(teacher)


if __name__ == '__main__':
    create_teachers()
