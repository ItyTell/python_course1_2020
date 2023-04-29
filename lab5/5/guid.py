import json
import csv
""""
44. Текстовий файл, записаний у форматі csv, містить інформацію щодо виконання студентами
лабораторних робіт у семестрі.
Записи файлу містять поля:
— номер залікової книжки (рядок з 6 цифр),
— навчальна група (рядок, не більше 6 символів),
— порядковий номер листа з лабораторною роботою (додатне ціле),
— код лабораторної роботи (рядок, від 1 до 7 символів),
— кількість балів за спробу (ціле від 0 до 10).
Допускаються білі рядки, які мають ігноруватися.
Студент однозначно ідентифікується заліковою книжкою. Жодний лист не містить дві лабораторні
одночасно.
До цього файлу додається додатковий файл, що містить інформацію:
— кількість записів основного файлу (ціле),
— сумарна кількість балів (ціле).
Додатковий файл записано у форматі json.
У цій задачі лабораторну вважати виконаною, якщо за неї отримано 6 або більше балів.
Балом, отриманим за лабораторну, вважати:
а) кількість балів найкращої спроби; FIND
б) кількість балів останньої спроби."""

""""
0012345, K12, 1, "code123", 0,   
"""
class Info:

    instance = None

    def __init__(self):
        self._students =[]

    def clear(self):
        self._students.clear()

    def push(self, student):
        st = None
        for x in self._students:
            if x._id == student._id:
                st = x
                break
        if st is None:
            self._students.append(student)
        else:
            l = student.labs[0]
            st.push(l)

       # self._students.append(student)


    @staticmethod
    def get_instance():
        if Info.instance is None:
            Info.instance = Info()
        return Info.instance


class Student:

    def __init__(self, id, grp):
        self._id = id
        self._grp = grp
        self.labs = []

    def get_summary(self):
        t = 0
        for i in self.labs:
            t += i._score
        return t

    def push(self, laba):
        tmp = None
        for x in self.labs:
            if x._code == laba._code:
                tmp = x
                break
        if tmp is None:
            self.labs.append(laba)
        else:
            if laba._score > tmp._score:
                tmp._score = laba._score
                tmp._best =  laba._best
            tmp._n = max(laba._n, tmp._n)




class Laba:
    def __init__(self, atempt, code, score):
        self._n = atempt
        self._code = code
        self._score = score
        self._best =atempt


class Loader:
    @staticmethod
    def load(file_path, info):
        info.clear()
        with open(file_path, 'r') as s_csv:
            r = csv.reader(s_csv)

            for row in r:
               # print("1", row)
                s = Student(int(row[0]), row[1])
                l = Laba(int(row[2]), row[3], int(row[4]))
                s.push(l)
                info.push(s)

    @staticmethod
    def write_json(info):
        total_score = 0
        total_stud = len(info._students)
        for x in info._students:
            total_score+=x.get_summary()

        return total_score, total_stud


Loader.load('studentslabs.csv', Info.get_instance())
print(Loader.write_json(Info.get_instance()))