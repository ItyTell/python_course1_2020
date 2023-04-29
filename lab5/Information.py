"""
The program was created by Nick Kolomiiets
"""

from Student import *


class Information():

    def __init__(self):
        self.student_list = {}

    def load(self, family_name, subject, group, second_name, name, mark, number, mark_100, ex_mark):
        """
        load the data into the classes and check if it is ok

        :param family_name: str
        family name of the student

        :param subject: str
        subject name

        :param group: str
        group inditificator

        :param second_name: str
        second name of the student

        :param name: str
        name of the student

        :param mark: int
        mark of the student in 5

        :param number: int
        number of the student

        :param mark_100: int
        mark of the student in 100

        :param ex_mark: int
        mark of the student for examen in 40
        """

        if self.__find(number):
            if self._check_if_data_incorrect(number, name, second_name, family_name, group):
                raise Exception('Two students have one number')
        else:
            self._add(number, name, second_name, family_name, group)

        self.student_list[number].load(subject, mark, ex_mark, mark_100)

    def __find(self, number):

        """
        finding student
        :param number: int
        number of the student
        :return: bool
        True if student is already created else False
        """

        if number in self.student_list:
            return True
        else:
            return False

    def _check_if_data_incorrect(self, number, name, second_name, family_name, group):

        """
        check if data is incorrect

        :param number: int
        number of the student

        :param name: str
        name of the student

        :param second_name: str
        second name of the student

        :param family_name: str
        family name of the student

        :param group: str
        group iditificator

        :return: bool
        False if data is correct and True else
        """

        if self.student_list[number].name == name and \
                self.student_list[number].second_name == second_name and \
                self.student_list[number].family_name == family_name and \
                self.student_list[number].group == group:
            return False
        else:
            return True

    def _add(self, number, name, second_name, family_name, group):
        """

        add new student

        :param number: int
        number of the student

        :param name: str
        name of the student

        :param second_name: str
        second name of the student

        :param family_name: str
        family name of the student

        :param group: str
        group inditificator

        """
        self.student_list[number] = Student(number, name, second_name, family_name, group)

    def output(self, result_path, codding):

        """
        find and write output to the file

        :param result_path: str
        path to the result file

        :param codding: str
        coding for writing file
        """

        print(f'output {result_path}:')
        self._write(result_path, codding)
        print(f'output {result_path}: OK')


    def clear(self):

        """
        clear all students property
        """

        for student in self.student_list.values():
            student.clear()
        self.student_list.clear()

    def _find_tales(self, student):

        """
        :param student: Student

        :return: (int, list, list)
        tales of the student
        list of subjects that he didn't pass well enough
        list of subjects that he didn't pass at all
        """

        tales = 0
        subject_list = []
        non_passed_subjects = []
        for subject in Student.subject_list.values():
            if not (student in subject.mark_list):
                tales += 1
                non_passed_subjects.append(subject)
            elif subject.mark_list[student] < 3 or subject.ex_mark_list[student] == 0 :
                tales += 1
                subject_list.append(subject)
        return tales, subject_list, non_passed_subjects

    def _write(self, result_path, codding):

        """
        write all the results
        :param result_path: str
        path to the result file

        :param codding: str
        coding to write the result file with
        """

        with open(result_path, 'w', encoding=codding) as file:
            for student in self.student_list.values():
                tales, subject_list, non_passed_subjects = self._find_tales(student)
                if tales > 0 and subject_list:
                    evarage_mark = self._avarage_mark(student)
                    self._write_data(file, student, subject_list, non_passed_subjects, tales, evarage_mark)

    def _avarage_mark(self, student):

        """
        calculate average mark od the student

        :param student: Student

        :return:
        average mark
        """

        s = 0
        i = 0
        for subject in Student.subject_list.values():
            if student in subject.mark_list:
                s += subject.mark_list[student]
                i += 1
        if i > 0:
            s /= i
        else:
            s = 0
        return round(s)

    def _write_data(self, file, student, subject_list, non_passed_subjects, tales, average_mark):

        """
        :param file: file
        file to write results

        :param student:Student

        :param subject_list: list
        list of subjects that he didn't pass well enough

        :param non_passed_subjects: list
        list of subjects that he didn't pass at all

        :param tales: int
        number of tales of the student

        :param average_mark: int
        average mark of the student
        """

        file.write(f"{average_mark} {tales} {student.number} {student.family_name} {student.name} {student.second_name}\n")
        for subject in subject_list:
            file.write(f"\t {subject.name} {subject.mark_list[student]}\n")
        for subject in non_passed_subjects:
            file.write(f"\t {subject.name}\n")


