# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы,
# а также реализуйте две функции:

# 1) для подсчета средней оценки за домашние задания по всем студентам в
# рамках конкретного курса (в качестве аргументов принимаем список
# студентов и название курса);
# 2) для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса)

class Mentor:
    # Создаём список преподователей :
    mentor_list = []
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # 'courses_attached'-'подключенные курсы'
        self.grades_dict_lecturer = {} # словарь с оценками лекторам от студентов
        self.average_grade = 0      # Средняя оценка за лекции
        self.mentor_list.append(self)  # Добавим в список преподователей вновь созданный экземпляр

class Student:
    # Создадим общий список студентов :
    student_list = []
    def __init__(self,name,surname,gender,):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.student_list.append(self) # Добавим в список студентов вновь созданный экземпляр
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
    def add_grades_lecturer(self, lecturer, course, grades):
        # Если лектор - экземпляр класса Lecturer , курс входит в список курсов ,которые
        # ведёт лектор и курс входит в список текущих курсов студента , то :
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades_dict_lecturer:
                lecturer.grades_dict_lecturer[course] += [grades]
            else:
                lecturer.grades_dict_lecturer[course] = [grades]
        else:
            print(f'Ошибка. Проверьте , является ли  {lecturer.name} {lecturer.surname} экземпляром'
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
            print(f'Ошибка. Проверьте , является ли  {student.name} {student.surname} экземпляром'
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
lecturer_1 = Lecturer('Егор','Седов')
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
student_4 = Student('Петр','Васильев','пацан')
student_4.courses_in_progress.append('Python Web')
student_5 = Student('Василиса','Прекраснова','девка')
student_5.courses_in_progress.append('Python Web')
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
# Вызов метода вычисления средней оценки  лектора_1
print(lecturer_1.average_grade_lectures()) # 9.33
# Проверка переопределения метода __str__ для лекторов:
print(lecturer_1)  # Имя: Егор
                   # Фамилия : Седов
                   # Средняя оценка за лекции: 9.33

# Зададим выставление оценок проверяющими (reviewer) студентам соответствующих курсов
reviewer_1 = Reviewer ('Иван','Петров')  # Проверяющий_1
reviewer_1.courses_attached.append('Python') # Добавили курс 'Python' в список проверяемых курсов
reviewer_1.courses_attached.append('Python Web')
reviewer_1.add_grades_student(student_1, 'Python', 10) # Добавили оценку -1 студенту-1
reviewer_1.add_grades_student(student_1, 'Python', 9)  # Добавили оценку -2 студенту-1
reviewer_1.add_grades_student(student_1, 'Python', 10) # Добавили оценку -3 студенту-1
print(f'Оценки для student_1 - {student_1.grades_dict_student }') # {'Python': [10, 9, 10]}
reviewer_1.add_grades_student(student_2, 'Python', 8) # Добавили оценку -1 студенту-2
reviewer_1.add_grades_student(student_2, 'Python', 9)  # Добавили оценку -2 студенту-2
reviewer_1.add_grades_student(student_2, 'Python', 9) # Добавили оценку -3 студенту-2
print(f'Оценки для student_2 - {student_2.grades_dict_student }') # {'Python': [10, 9, 10]
reviewer_1.add_grades_student(student_3, 'Python', 8)
reviewer_1.add_grades_student(student_3, 'Python', 9)
reviewer_1.add_grades_student(student_3, 'Python', 8)
print(f'Оценки для student_3 - {student_3.grades_dict_student }')

reviewer_1.add_grades_student(student_4, 'Python Web', 8)
reviewer_1.add_grades_student(student_4, 'Python Web', 7)
reviewer_1.add_grades_student(student_4, 'Python Web', 8)
print(f'Оценки для student_4 - {student_4.grades_dict_student }')

reviewer_1.add_grades_student(student_5, 'Python Web', 6)
reviewer_1.add_grades_student(student_5, 'Python Web', 8)
reviewer_1.add_grades_student(student_5, 'Python Web', 6)
print(f'Оценки для student_5 - {student_5.grades_dict_student }')

# Проверка - Средняя оценка для student_1:
print(student_1.average_grade_student()) # 9.67

# Добавим курс в список текущих курсов студентов
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

#  Функция для подсчета средней оценки за домашние задания по всем
#  студентам в рамках конкретного курса (в качестве аргументов принимаем список
#  студентов и название курса)
def get_average_grade_student_course (other_list,course):
    # Cоздаём пустой список оценок всех студентов конкретного курса:
    all_grades_list_course = []
    for student in other_list:
        for key, vul in student.grades_dict_student.items():
            if key == course:
                # Добавим в общий список оценок оценки конкретного студента
                all_grades_list_course.extend(vul)
    # Сумма всех оценок студентов данного курса
    sum_ = sum(all_grades_list_course)
    # Средняя оценка
    average_grade_student = round(sum_ / len(all_grades_list_course), 2)
    return average_grade_student
# Проверка работы функции для подсчёта средней оценки за ДЗ студентов для 2-х курсов :
print(get_average_grade_student_course (Student.student_list,"Python")) # 8.89
print(get_average_grade_student_course (Student.student_list,'Python Web')) # 7.17

# Часть 2
# Функция , формирующая список курсов лекторов
def get_lecturer_course(other_list):
    lecturer_course_all = []
    for mentor in other_list:
        if len(mentor.grades_dict_lecturer) > 0: # Убираем проверяющих из списка преподавателей
            lecturer_course_all.extend(mentor.courses_attached)
    lecturer_course_list = list(set(lecturer_course_all))
    return lecturer_course_list
# Проверка
print(get_lecturer_course(Mentor.mentor_list)) # ['Python']

# Функция для подсчета средней оценки за лекции всех лекторов c проверкой
# (в качестве аргумента принимаем список лекторов и название курса)
def get_average_grade_mentor_course (other_list,course):
    # Вызываем список курсов лекторов
    lecturer_course_list = get_lecturer_course(other_list)
    # Проверяем, входит ли подаваемый на вход функции курс в список курсов лекторов
    if course not in lecturer_course_list :
        print('Ошибка.Такого курса нет в списке курсов лекторов')
        return
    all_grades_lecturer_course = [] # Список оценок лекторов
    for lecturer in other_list:
        if len(lecturer.grades_dict_lecturer) > 0:
            for key, vul in lecturer.grades_dict_lecturer.items():
                if key == course:
                    all_grades_lecturer_course.extend(vul) # Заполняем список оценок лекторов
    # Сумма всех оценок лекторов данного курса
    sum_ = sum(all_grades_lecturer_course)
    # Средняя оценка
    average_grade_lecturer = round(sum_ / len(all_grades_lecturer_course), 2)
    return average_grade_lecturer
# Вызываем функцию для подсчета средней оценки за лекции всех лекторов
print(get_average_grade_mentor_course(Mentor.mentor_list,'Python')) # 8.83
# Проверка при неправильном введении курса :
print(get_average_grade_mentor_course(Mentor.mentor_list,'ython'))  # Ошибка.Такого курса нет в списке курсов лекторов












