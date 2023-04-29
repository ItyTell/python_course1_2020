import json

import csv

import sys


class Information:

    def __init__(self):
        pass

    def add_student(self, number, name, second_name, family_name, group):
        Student(number, name, second_name, family_name, group)

    def clear(self):
        Student.list_of_students = []
        Subject.list_of_subjects = []

    def output(self, res, coding):
        print(f'output {res}:')
        for student in Student.list_of_students:
            tale = 0
            sbj_list = []
            for subject in Subject.list_of_subjects:
                mark = subject.marks_100[student]
                if mark < 60:
                    tale += 1
                    sbj_list.append((subject, mark, subject.marks[student]))
            if tale > 0:
                s = 0
                for i in sbj_list:
                    s += i[1]
                s /= len(sbj_list)
                print(int(s), tale, student.number, student.family_name, student.name, student.family_name)
                for i in sbj_list:
                    print('    ', i[0].name, i[2])
        print(f'output {res}: OK')


    def __find(number):
        x = False
        for student in Student.list_of_students:
            if student.number == number:
                x = student
        return x

    def __add(number, name, second_name, family_name, group):
        Student(number, name, second_name, family_name, group)

    def load(self, family_name, subject, group, second_name, name, mark, number, mark_100, ex_mark):
        student = Information.__find(number)
        if student:
            if not (student.name == name and student.second_name == second_name and
                    student.family_name == family_name and student.group == group):
                raise Exception
        else:
            Information.__add(number, name, second_name, family_name, group)
            student = Information.__find(number)
        student.load(subject, mark, ex_mark, mark_100)


class Student():
    list_of_students = []

    def __init__(self, number, name, second_name, family_name, group):
        self.number = number
        self.name = name
        self.second_name = second_name
        self.family_name = family_name
        self.group = group
        Student.list_of_students.append(self)

    def __find(subject):
        x = False
        y = None
        for i in Subject.list_of_subjects:
            if not x and i.name == subject:
                x = True
                y = i
        return (x, y)

    def __add(subject):
        Subject(subject)

    def load(self, subject, mark, ex_mark, mark_100):
        if not (Student.__find(subject)[0]):
            Student.__add(subject)
        Student.__find(subject)[1].load(mark, ex_mark, mark_100, self)


class Subject():
    list_of_subjects = []

    def __init__(self, name):
        self.name = name
        self.marks = {}
        self.ex_marks = {}
        self.marks_100 = {}
        Subject.list_of_subjects.append(self)

    def load(self, mark, ex_mark, mark_100, student):
        self.marks[student] = float(mark)
        self.ex_marks[student] = float(ex_mark)
        self.marks_100[student] = float(mark_100)


class Builder():

    def __init__(self):
        self.main_list = []
        self.second_list = []

    def clear(self):
        self.main_list = []
        self.second_list = []

    def load(self):
        for line in self.main_list:
            family_name = line[0]
            subject = line[1]
            group = line[2]
            second_name = line[3]
            name = line[4]
            mark = line[5]
            number = line[6]
            mark_100 = line[7]
            ex_mark = line[8]
            information.load(family_name, subject, group, second_name, name, mark, number, mark_100, ex_mark)


information = Information()
builder = Builder()


def load_settings(task):
    print('виконується завантаження файлу з налаштуваннями')
    with open(task, 'r') as configfile:
        settings = json.load(configfile)
    try:
        settings['input']['json']
        settings['input']['csv']
        settings['input']['encoding']
        settings['output']['fname']
        settings['output']['encoding']
    except:
        raise Exception
    print(f'ini {task}: OK')
    load(information, settings['input']['csv'], settings['input']['json'], settings['input']['encoding'], builder)


def load_data(csv_file, inf_obj, coding_type, builder):
    inf_obj.clear()
    builder.clear()
    print('виконується завантаження основного файлу')
    try:
        with open(csv_file, encoding=coding_type) as file:
            builder.main_list = []
            reader = csv.reader(file, delimiter=';')
            for line in reader:
                builder.main_list.append(line)
    except:
        builder.clear()
        raise Exception
    print(f'input-csv {csv_file}: OK')


def load_stat(json_file, inf_obj, coding_type, builder):
    with open(json_file, encoding=coding_type) as jfile:
        print('виконується завантаження допоміжного файлу')
        data = json.load(jfile)
        print(f'input-json {json_file}: ОК')
    try:
        builder.second_list = {'5': data["кількість оцінок 'відмінно'"], '3': data["кількість оцінок 'задовільно'"], 'all': data['загальна кількість записів']}
    except:
        raise Exception


def load(inf_obj, csv_file, json_file, coding_type, builder):
    load_data(csv_file, inf_obj, coding_type, builder)
    load_stat(json_file, inf_obj, coding_type, builder)
    if fit():
        print('json?=csv: OK')
    else:
        print('json?=csv: UPS')
    builder.load()


def info_about_me():
    print("Mykola Kolomiiets, K-12")


def goal_of_the_progtam():
    print('''Варіант № 79

    Обробляються результати складання студентами екзаменів зимової сесії
    
    Записи основного файлу містять поля: прізвище, предмет, код групи, по-батькові, ім'я, оцінка за
    державною шкалою, номер залікової книжки, сумарна оцінка в балах за 100-бальною системою, набрані
    на екзамені бали
    
    У допоміжному файлі наявні ключі: кількість оцінок «відмінно», кількість оцінок «задовільно», за-
    гальна кількість записів
    
    Знайти всіх студентів, що щось не склали. Вивести по кожному з них інформацію
    -- на першому рядку:
    
    середній бал (округлений до цілого), кількість хвостів, номер залікової книжки, прізвище, ім'я,
    по-батькові.
    щ- на наступних рядках, починаючи з табуляції, вивести для студента всі його результати (по одному
    на рядок)
    
    предмет, державна оцінка прописом
    сортуванні: державна оцінка прописом (впорядковуємо як рядки), предмет.''')


def fit():
    print('виконується перевірка відповідності основного та допоміжного файлів')
    best_mark = 0
    good_mark = 0
    quontity = 0
    for line in builder.main_list:
        quontity += 1
        if int(line[5]) == 5:
            best_mark += 1
        if int(line[5]) >= 3:
            good_mark += 1
    return best_mark == builder.second_list['5'] and good_mark == builder.second_list['3'] and quontity == builder.second_list['all']



def main(task):
    """try:"""
    load_settings(task)
    """except Exception as e:
        print('***** program aborted *****')
        print(e)
"""


task = sys.argv
info_about_me()
goal_of_the_progtam()
print("*****")
if len(task) == 1:
    main("task.ini")
else:
    print('***** program aborted *****')
    print('за бажанням вивести довідку з використання програми')


information.output("res.txt", "utf-8")