class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.course_attached = []


class Lecturer(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_score = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}'

    def average_grade(self):
        total_grades = 0
        count = 0
        for drades in self.course_score.values():
            total_grades += sum(drades)
            count += len(drades)
        return round(total_grades / count, 1) if count > 0 else 0

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()


class Reviewer(Mentors):
    def set_lection_score(self, student, homework, score):
        student.set_homework_score(homework, score)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.course_attached and student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.course_score:
                lecturer.course_score[course] += [grade]
            else:
                lecturer.course_score[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия {self.surname} \nСредняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')

    def average_grade(self):
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
            return round(total_grades / count, 1) if count > 0 else 0

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

def average_grade_course(students, course_name): #Функция для определения средней оценки на курсе по всем студентам
    total_grade = 0
    count = 0
    for student in students:
        if course_name in student.grades:
            total_grade += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    return round(total_grade / count, 1) if count > 0 else 0

def average_grade_lecturer(lecturers, course_name):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course_name in lecturer.course_score:
            total_grade += sum(lecturer.course_score[course_name])
            count += len(lecturer.course_score[course_name])
    return round(total_grade / count, 1) if count > 0 else 0


lecturer_1 = Lecturer('Alexandr', 'Fillipov')
lecturer_1.course_attached += ['PHP', 'JS']

lecturer_2 = Lecturer('Segey', 'Antipov')
lecturer_2.course_attached += ['Phyton', 'GO']

student_1 = Student('Alexandr', 'Kaigorodov', 'male')
student_1.courses_in_progress += ['PHP']
student_1.rate_lc(lecturer_1, 'PHP', 3)

student_2 = Student('Diana', 'Ovechkina', 'Female')
student_2.courses_in_progress += ['GO']
student_2.rate_lc(lecturer_2, 'GO', 7)

reviewer_1 = Reviewer('Dmitrii', 'Shavrov')
reviewer_1.course_attached += ['PHP']
reviewer_1.rate_hw(student_1, 'PHP', 3)

reviewer_2 = Reviewer('Ilya', 'Baikin')
reviewer_2.course_attached += ['GO']
reviewer_2.rate_hw(student_2, 'GO', 4)

print(reviewer_1)
print()

print(reviewer_2)
print()

print(lecturer_1)
print()

print(lecturer_2)
print()

print(student_1)
print()

print(student_2)
print()

if student_2 < student_1:
    print(f'Первый ученик отстает!!!!')
else:
    print("Второй ученик отстает!!!!")

lecturers = [lecturer_1, lecturer_2]
students = [student_1, student_2]

print(average_grade_lecturer(lecturers, 'PHP')) #Средняя оценка за домашку по курсу ПХП
print(average_grade_course(students, 'GO')) # Средняя оценка за лекцию по ГО



