"""
The program was created by Nick Kolomiiets
"""

from Subject import *


class Student():
    subject_list = {}

    def __init__(self, number, name, second_name, family_name, group):
        self.number = number
        self.name = name
        self.second_name = second_name
        self.family_name = family_name
        self.group = group
        self.subject_list = []

    def load(self, subject, mark, ex_mark, mark_100):
        """
        loading information about students' marks and add new subjects if needed

        :param subject: str
        name of the subject

        :param mark: int
        student's mark for the subject (from 0 to 5) depending in mark_100

        :param ex_mark: int
        student's mark for the examen of the subject (from 0 to 40) can not be from 1 to 24

        :param mark_100: int
        student's mark for the subject (from 0 to 100) depending on ex_mark

        :return: None
        """
        if self._find(subject):
            if self._check_marks(subject):
                raise Exception('Someone took the examen more then once')
        else:
            self._add(subject)
        Student.subject_list[subject].load(self, mark, ex_mark, mark_100)

    def _find(self, subject):

        """
        find subject

        :param subject: Subject
        needed to be found

        :return: Bool
        True if it exist
        False else
        """

        if subject in Student.subject_list:
            return True
        else:
            return False

    def _add(self, subject):

        """
        add a subject

        :param subject: Subject
        subject needed to be created
        """

        Student.subject_list[subject] = Subject(subject)

    def _check_marks(self, subject):

        """
        check if someone took the examen more then once

        :param subject: Subject

        :return: Bool
        True if someone took the examen more then once False else
        """

        if self in Student.subject_list[subject].mark_list:
            return True
        else:
            return False

    def clear(self):

        """
        clear all the information that was saved in Student class
        """

        for subject in Student.subject_list.values():
            subject.clear
        self.number = None
        self.name = None
        self.second_name = None
        self.family_name = None
        self.group = None
        self.subject_list.clear()
