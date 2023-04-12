# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy

# У лекторов:
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9

# У студентов :
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

# 2) Реализуйте возможность сравнивать (через операторы сравнения)
# между собой лекторов по средней оценке за лекции и студентов по
# средней оценке за домашние задания.

class Mentor:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # 'courses_attached'-'подключенные курсы'
        self.grades_dict_lecturer = {} # словарь с оценками лекторам от студентов
        self.average_grade = 0      # Средняя оценка за лекции


class Student:
    def __init__(self,name,surname,gender,):
        self.name=name
        self.surname = surname
        self.gender=gender
        self.finished_courses = []
        self.courses_in_progress = []  # 'изучаемые на данный момент курсы'
        self.grades_dict_student = {}  # словарь с оценками студентов от проверяющих
        self.average_grade = 0 # Средняя оценка за ДЗ

        # Метод для добавления пройденных курсов
    def add_courses (self,course_name):
        self.finished_courses.append(course_name)

    # Метод вычисления средней оценки за ДЗ :
    def average_grade_student(self):
        grade_list=[]
        for val in self.grades_dict_student.values():
            grade_list.extend(val)
        # Подсчитаем сумму оценок:
        sum_=sum(grade_list)
        # Подсчитаем среднее значение всех оценок
        self.average_grade = round(sum_/len(grade_list),2)
        return self.average_grade

    # Метод выставления оценок студентами лекторам
    # student_1.add_grades_lecturer(lecturer_1, 'Python', 9)
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

    # метод __str__ для Student :
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\nСредняя ' \
              f'оценка за ДЗ: {self.average_grade_student()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    #  Метод сравнения средних оценок студентов:
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade < other.average_grade


# Дочерние для класса Mentor классы Lecturer (лекторы) и Reviewer(проверяющие)
class Lecturer(Mentor):

    # Метод вычисления средней оценки за лекции :
    def average_grade_lectures(self):
        grade_list=[]
        for val in self.grades_dict_lecturer.values():
            grade_list.extend(val)
        # Подсчитаем сумму оценок:
        sum_=sum(grade_list)
        # Подсчитаем среднее значение всех оценок
        self.average_grade = round(sum_/len(grade_list),2)
        return self.average_grade

    #  Метод сравнения средних оценок лекторов :
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade < other.average_grade


    # метод __str__ для Lecturer :
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\nСредняя ' \
              f'оценка за лекции: {self.average_grade_lectures()}'
        return res


class Reviewer(Mentor):
    # Метод , который позволяет проверяющему добавить оценку в словарь студента
    # по названию курса
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
    # метод __str__ для Reviewer :
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия = {self.surname}'
        return res
# Проверка метода __str__ для проверяющих:
reviewer_1 = Reviewer ('Иван','Петров')
print(reviewer_1)                        # Имя: Иван
                                         # Фамилия = Петров
# Инициализация лекторов :
(lecturer_1) = Lecturer('Егор','Седов')
lecturer_1.courses_attached.append('Python')
lecturer_2 = Lecturer('Анна','Федотова')
lecturer_2.courses_attached.append('Python')
# Инициализация студентов :
student_1= Student('Вася','Пупкин','пацан')
student_1.courses_in_progress.append('Python')
student_2= Student('Ольга','Зуева','девка')
student_2.courses_in_progress.append('Python')
student_3= Student('Елена','Белая','девка')
student_3.courses_in_progress.append('Python')
# Выставим оценки лектору-1
student_1.add_grades_lecturer(lecturer_1, 'Python', 9)
student_2.add_grades_lecturer(lecturer_1, 'Python', 9)
student_3.add_grades_lecturer(lecturer_1, 'Python', 10)
# Выставим оценки лектору-2
student_1.add_grades_lecturer(lecturer_2, 'Python', 9)
student_2.add_grades_lecturer(lecturer_2, 'Python', 8)
student_3.add_grades_lecturer(lecturer_2, 'Python', 8)
# Посмотрим оценки обоих лекторов(проверка):
print(lecturer_1.grades_dict_lecturer) # {'Python': [9, 9, 10]}
print(lecturer_2.grades_dict_lecturer) # {'Python': [9, 8, 8]}
# Вызов метода вычисления средней оценки лектора_1
print(lecturer_1.average_grade_lectures()) # 9.33
# Проверка переопределения метода __str__ для лекторов:
print(lecturer_1)  # Имя: Егор
                   # Фамилия : Седов
                   # Средняя оценка за лекции: 9.33
# Инициализируем проверяющих
reviewer_1 = Reviewer ('Иван','Петров')  # Проверяющий_1
reviewer_1.courses_attached.append('Python') # Добавили курс 'Python' в список проверяемых курсов
# Зададим выставление оценок проверяющими (reviewer) студентам соответствующих курсов
reviewer_1.add_grades_student(student_1, 'Python', 10) # Добавили оценку -1 студенту-1
reviewer_1.add_grades_student(student_1, 'Python', 9)  # Добавили оценку -2 студенту-1
reviewer_1.add_grades_student(student_1, 'Python', 10) # Добавили оценку -3 студенту-1
print(f'Оценки для student_1 - {student_1.grades_dict_student }') # {'Python': [10, 9, 10]}
reviewer_1.add_grades_student(student_2, 'Python', 8) # Добавили оценку -1 студенту-1
reviewer_1.add_grades_student(student_2, 'Python', 9)  # Добавили оценку -2 студенту-1
reviewer_1.add_grades_student(student_2, 'Python', 9) # Добавили оценку -3 студенту-1
print(f'Оценки для student_2 - {student_2.grades_dict_student }') # {'Python': [10, 9, 10]
# Проверка - Средняя оценка для student_1:
print(student_1.average_grade_student()) # 9.67
# Добавим курс в список текущих курсов
student_1.courses_in_progress.append('Git')
print(student_1.courses_in_progress)
# Добавим курс в список оконченных курсов :
student_1.finished_courses.append('Введение в программирование')
# Проверка переопределения метода __str__ для студентов:
print(student_1) # Имя: Вася
                 # Фамилия : Пупкин
                 # Средняя оценка за ДЗ: 9.67
                 # Курсы в процессе изучения: Python, Git
                 # Завершенные курсы: Введение в программирование


# 2) Реализуйте возможность сравнивать (через операторы сравнения)
# между собой лекторов по средней оценке за лекции и студентов по
# средней оценке за домашние задания.

# Проверим словари с оценками у лекторов:
print (lecturer_1.grades_dict_lecturer) # {'Python': [9, 9, 10]}
print (lecturer_2.grades_dict_lecturer) # {'Python': [9, 8, 8]}
# Средние оценки лекторов 1 и 2 :
lecturer_1.average_grade = lecturer_1.average_grade_lectures()
lecturer_2.average_grade = lecturer_2.average_grade_lectures()
print(lecturer_1.average_grade,lecturer_2.average_grade) # 9.33 8.33
# Производим сравнение лекторов по средним оценкам за лекции
print(lecturer_1 < lecturer_2) # False

# Средние оценки студентов 1 и 2 :
student_1.average_grade = student_1.average_grade_student()
student_2.average_grade = student_2.average_grade_student()
print(student_1.average_grade,student_2.average_grade) # 9.67 8.67
# Сравним студентов по средней оценке по ДЗ :
print(student_1 > student_2) # True

