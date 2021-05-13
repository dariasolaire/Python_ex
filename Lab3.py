""""" Определить пользовательский класс в соответствии с вариантом задания

1)	определить в классе следующие конструкторы: с параметрами и без параметров
2)	компоненты-функции для просмотра и установки полей данных: setТип(),
getТип() (помним про инкапсуляцию проверку корректности задания параметров);
3)	написать демонстрационную программу, в которой создаются и разрушаются объекты (от 3 до 5 шт.)
и указатели на объекты пользовательского класса и каждый вызов конструктора сопровождается выдачей соответствующего сообщения.
4)	использовать метод __setattr__()""5)	не забывайте выполнять задание, выделенное курсивом в варианте.

Создать класс Student: id, Фамилия, Имя,  Отчество, Дата рождения, Адрес, Телефон, Факультет, Курс, Группа.
 Функции-члены реализуют запись и считывание полей (проверка корректности),
 расчет возраста студента Создать список объектов. Вывести:
a) список студентов заданного факультета;
d) список учебной группы."""


class Student:
    university='БГУ'
    def __init__(self,
                 id='0',
                 surname='0',
                 name='0',
                 last_name='0',
                 date_birthday='0',
                 adress='0',
                 phone_number='0',
                 faculty='0',
                 course='0',
                 group='0'):
        self.__id = id
        self.__surname = surname
        self.__name = name
        self.__last_name = last_name
        self.__date_birthday = date_birthday
        self.__adress = adress
        self.__phone_number = phone_number
        self.__faculty = faculty
        self.__course = course
        self.__group = group
        print('Вызван конструктор __init__')

    def __del__(self):  # Деструктор класса
        print('Вызван метод __del__()')

    def __setattr__(self, attr, value):
        if attr != 'БГУ':
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_surnsme(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_date_birthday(self):
        return self.__date_birthday

    def set_date_birthday(self, date_birthday):
        self.__date_birthday = date_birthday

    def get_adress(self):
        return self.__adress

    def set_adress(self, adress):
        self.__adress = adress

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_faculy(self):
        return self.__faculty

    def set_faculty(self, faculty):
        self.__faculty = faculty

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def get_group(self):
        return self.__group

    def set_group(self, group):
        self.__group = group


Student_list = [
    Student('0001', 'Иванов', 'Василий', 'Павлович', '01.12.1999', 'РБ, г.Витебск, Октябрьская, 5', '80291111111',
            'математики', '4', '402'),
    Student('0015', 'Рыжова', 'Алиса', 'Михайловна', '02.10.2000', 'РБ, г.Минск, Захарова, 8', '80442559865',
            'естетвознания', '3', '301'),
    Student('0108', 'Болотников', 'Андрей', 'Заирович', '05.05.2001', 'РБ, г.Минск, Харьковская, 25', '804425552147',
            'информатики', '3', '303'),
    Student('0025', 'Котькина', 'Анна', 'Степановна', '09.12.1999', 'РБ, г.Могилев, Советская, 12', '8029115891',
            'математики', '4', '402'),
    Student('0030', 'Инина', 'Ирина', 'Игоревна', '02.05.2000', 'РБ, г.Минск, Одинцова, 8', '80442559865',
            'естетвознания', '3', '301'),
    Student('0205', 'Бобов', 'Мурад', 'Тахирович', '05.08.2001', 'РБ, г.Минск, Харьковская, 25', '804425552147',
            'информатики', '3', '303')
]

def print_list(obj_list, param):
    if len(obj_list) > 0:
        print(f'Результат по критерию "{param}":')
        for obj in obj_list:
            print(obj.get_id(), obj.get_surnsme(), obj.get_name(), obj.get_last_name(), obj.get_date_birthday(), obj.get_adress(), obj.get_phone_number(), obj.get_faculy(), obj.get_group(), obj.get_course())
        return

def show_result(arg, lambda_exp):
    filter_result = list(filter(lambda_exp, Student_list))
    print_list(filter_result, arg) if len(filter_result) > 0 else print('Данных по запросу не найдено')

group_request = input('Введите номер группы: \n')
show_result(group_request, lambda x: x.get_group() == group_request)

faculty_request = input('Введите интересующий факультет: \n')
show_result(faculty_request, lambda x: x.get_faculty() == faculty_request)
