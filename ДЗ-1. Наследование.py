# Исходя ДЗ-0 , у нас уже есть класс преподавателей
# и класс студентов . Студентов пока оставим без изменения, а вот преподаватели бывают разные,
# поэтому теперь класс Mentor должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы)
# и Reviewer (эксперты, проверяющие домашние задания).
# Очевидно, имя, фамилия и список закрепленных курсов логично реализовать
# на уровне родительского класса.

class Student:
    def __init__(self,name,surname,gender):
        self.name=name
        self.surname= surname
        self.gender=gender
        self.finished_courses = []
        self.courses_in_progress = []  # 'изучаемые на данный момент курсы'
        self.grades_dict = {}            # 'grades' - 'оценки'
    # Добавим классу Student метод для добавления пройденных курсов
    def add_courses (self,course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # 'courses_attached'-'подключенные курсы'

    # Метод выставления оценок студентам .

    def add_grades(self,student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades_dict:
                student.grades_dict[course] +=[grades]
            else:
                student.grades_dict[course] = [grades]
        else:
            print(f'Ошибка. Проверте , является ли  {student.name} {student.surname} экземпляром'
                  f' класса Student , входит ли "{course}" в список курсов , которые на данный момент'
                  f' изучает студент {student.name} {student.surname} '
                  f' и  является ли "{course}" - курсом , на котором преподаёт'
                  f' {self.name} {self.surname}')

# Создаём дочерние для класса Mentor классы Lecturer (лекторы) и Reviewer
class Lecturer(Mentor):
    pass
class Reviewer(Mentor):
    pass
# Проверка :
lecturer_1 = Lecturer('Елена','Никитина')
lecturer_1.courses_attached.append('Словарики')

reviewer_1 = Reviewer ('Иван','Петров')
reviewer_1.courses_attached.append('Python')

print(lecturer_1.name)                # Елена
print(lecturer_1.surname)             # Никитина
print(lecturer_1.courses_attached)    # ['Словарики']

print(reviewer_1.name)                # Иван
print(reviewer_1.surname)             # Петров
print(reviewer_1.courses_attached)    # ['Python']
