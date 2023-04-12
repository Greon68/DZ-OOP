# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам
# оценки за домашние задания. Теперь это могут делать только Reviewer (реализуйте такой метод)!
# А что могут делать лекторы? Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student
# (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer,
# в котором ключи – названия курсов, а значения – списки оценок).
# Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

class Mentor:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # 'courses_attached'-'подключенные курсы'
        self.grades_dict_lecturer = {} # словарь с оценками лекторам от студентов


class Student:
    def __init__(self,name,surname,gender):
        self.name=name
        self.surname= surname
        self.gender=gender
        self.finished_courses = []
        self.courses_in_progress = []  # 'изучаемые на данный момент курсы'
        self.grades_dict_student = {}            # 'grades' - 'оценки'
    # Метод для добавления пройденных курсов
    def add_courses (self,course_name):
        self.finished_courses.append(course_name)

    # Метод выставления оценок студентами лекторам
    def add_grades_lecturer(self, lecturer, course, grades):
        # Если лектор - экземпляр класса Lecturer , курс входит в список курсов ,которые
        # ведёт лектор и курс входит в список текущих курсов студента :
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades_dict_lecturer:
                lecturer.grades_dict_lecturer[course] += [grades]
            else:
                lecturer.grades_dict_lecturer[course] = [grades]
        else:
            print(f'Ошибка. Проверте , является ли  {lecturer.name} {lecturer.surname} экземпляром'
                  f' класса Student , входит ли "{course}" в список курсов , которые на данный момент'
                  f' изучает студент {lecturer.name} {lecturer.surname} '
                  f' и  является ли "{course}" - курсом , на котором преподаёт'
                  f' {self.name} {self.surname}')




# Создаём дочерние для класса Mentor классы Lecturer (лекторы) и Reviewer
class Lecturer(Mentor):
    pass

class Reviewer(Mentor):
    # Метод , который позволяет добавить оценку проверяющим в словарь студента по названию курса
    def add_grades_student(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades_dict_student:
                student.grades_dict_student[course] += [grades]
            else:
                student.grades_dict_student[course] = [grades]
        else:
            print(f'Ошибка. Проверте , является ли  {student.name} {student.surname} экземпляром'
                  f' класса Student , входит ли "{course}" в список курсов , которые на данный момент'
                  f' изучает студент {student.name} {student.surname} '
                  f' и  является ли "{course}" - курсом , на котором преподаёт'
                  f' {self.name} {self.surname}')

student_1= Student('Вася','Пупкин','пацан')
student_1.courses_in_progress.append('Python')
# Зададим выставление оценок проверяющими (reviewer) студентам соответствующих курсов
reviewer_1 = Reviewer ('Иван','Петров')  # Проверяющий -1
reviewer_1.courses_attached.append('Python') # Добавили курс 'Python' в список проверяемых курсов

reviewer_1.add_grades_student(student_1, 'Python', 10) # Добавили оценку -1 студенту-1
reviewer_1.add_grades_student(student_1, 'Python', 9)  # Добавили оценку -2 студенту-1
reviewer_1.add_grades_student(student_1, 'Python', 10) # Добавили оценку -3 студенту-1
# Проверка :
# Студент-1
print(student_1.name)
print(student_1.surname)
print(student_1.gender)
print(student_1.courses_in_progress)
print(student_1.grades_dict_student)
# Проверяющий -1
print(reviewer_1.name)
print(reviewer_1.surname)
print(reviewer_1.courses_attached)
# Зададим выставление оценок студентами лекторам
# Инициализируем лектора :
lecturer_1 = Lecturer('Егор','Седов')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Python-WEB')

# Инициализируем студентов :
student_2= Student('Ольга','Зуева','девка')
student_2.courses_in_progress.append('Python')
student_3= Student('Елена','Белая','девка')
student_3.courses_in_progress.append('Python')
student_4= Student('Сергей','Большов','пацан')
student_4.courses_in_progress.append('Python-WEB')
student_5= Student('Олег','Крутой','пацан')
student_5.courses_in_progress.append('Python-WEB')
# Выставим оценки лектору-1 :
student_1.add_grades_lecturer(lecturer_1, 'Python', 9)
student_2.add_grades_lecturer(lecturer_1, 'Python', 9)
student_3.add_grades_lecturer(lecturer_1, 'Python', 10)
student_4.add_grades_lecturer(lecturer_1, 'Python-WEB', 10)
student_5.add_grades_lecturer(lecturer_1, 'Python-WEB', 7)
# Проверка
print(lecturer_1.courses_attached)  # Курсы лектора-1 - ['Python', 'Python-WEB']
print(lecturer_1.grades_dict_lecturer)  # Оценки от студентов - {'Python': [9, 9, 10], 'Python-WEB': [10, 7]}

