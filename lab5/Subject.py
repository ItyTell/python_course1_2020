"""
The program was created by Nick Kolomiiets
"""


class Subject():
    def __init__(self, subject):
        self.name = subject
        self.mark_list = {}
        self.ex_mark_list = {}
        self.mark_100_list = {}

    def load(self, student, mark, ex_mark, mark_100):
        """
        load marks for exact subject for exact student

        :param student: Student
        object that contains information about student

        :param mark: int
        student's mark for the subject (from 0 to 5) depending in mark_100

        :param ex_mark: int
        student's mark for the examen of the subject (from 0 to 40) can not be from 1 to 24

        :param mark_100: int
        student's mark for the subject (from 0 to 100) depending on ex_mark
        """

        self.mark_list[student] = mark
        self.ex_mark_list[student] = ex_mark
        self.mark_100_list[student] = mark_100

    def clear(self):

        """
        clear all the information that was saved in Subject class
        """

        self.name = None
        self.mark_list.clear
        self.ex_mark_list.clear()
        self.mark_100_list.clear()
