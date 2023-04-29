"""
The program was created by Nick Kolomiiets
"""



import json

import csv

from Information import *

import re


def _space(string):
    if (string[0] == ' ') or (string[len(string) - 1] == ' '):
        return True
    else:
        return False


class Builder():

    def load(self, file, information):
        """
        load information about students
        :param file: file
        file the is needed to load
        :param information:
        :return:
        """
        reader = csv.reader(file, delimiter=';')
        for object in reader:
            if len(object) == 0:
                continue
            self._load_properties(object)
            result = self._check_properties()
            if result[0]:
                raise Exception('Problem with format of ' + result[1] + ": " + result[2])

            information.load(self.family_name, self.subject, self.group, self.second_name, self.name, self.mark,
                             self.number, self.mark_100, self.ex_mark)

    def _load_properties(self, object):

        """
        :param object: list
        line in the general file
        """

        self.family_name = object[0]
        self.subject = object[1]
        self.group = object[2]
        self.second_name = object[3]
        self.name = object[4]
        self.mark = object[5]
        self.number = object[6]
        self.mark_100 = object[7]
        self.ex_mark = object[8]

    def _check_properties(self):

        """

        pattern_name check, pattern_second_name, pattern_subject: if it contains right number of letters or numbers or defice or space (then check that it will not contain numbers)

        pattern_search_number: check if it contains numbers

        pattern_group: if it contains right number of letters or numbers or defice or space

        pattern_number: check if contains 8 numbers


        :return: False if data is Ok
                 else True
        """

        pattern_name = re.compile(r"[\w\- ]{1,20}")
        pattern_second_name = re.compile(r"[\w\- ]{1,27}")
        pattern_subject = re.compile(r'[\w"\- ]{4,57}')
        pattern_search_number = re.compile(r"[\d]")
        pattern_group = re.compile(r'[\w\- ]{1,7}')
        pattern_number = re.compile(r'[\d]{8}')

        result = (False, None, None)
        if not pattern_name.fullmatch(self.name) or pattern_search_number.search(self.name) or _space(self.name):
            result = (True, 'name', self.name)

        if not pattern_name.fullmatch(self.family_name) or pattern_search_number.search(self.family_name) or _space(self.family_name):
            result = (True, 'family name', self.family_name)

        if not pattern_second_name.fullmatch(self.second_name) or pattern_search_number.search(self.second_name) or _space(self.second_name):
            result = (True, 'second name', self.second_name)

        if not pattern_subject.fullmatch(self.subject) or pattern_search_number.search(self.subject) or _space(self.subject):
            result = (True, 'subject', self.subject)

        if not pattern_group.fullmatch(self.group) or _space(self.group):
            result = (True, 'group', self.group)

        if len(self.number) != 7:
            result = True
            result = (True, 'number', self.number)

        try:
            self.mark = int(self.mark)
            self.number = int(self.number)
            self.mark_100 = int(self.mark_100)
            self.ex_mark = int(self.ex_mark)
        except:
            result = (True, 'mark or number:', "it is not an integer")

        if not self._check_marks():
            result = (True, 'marks','harmonization of the marks')

        return result

    def _check_marks(self):

        """
        :return: True if data is correct
                 else False
        """

        result = False

        if 40 > self.ex_mark > self.mark_100 - 61 and (
                self.ex_mark > 23 or self.ex_mark == 0) and 100 > self.mark_100 > 0 and self.mark > 0:
            if self.mark == 5 and self.mark_100 > 89:
                result = True

            elif self.mark == 4 and 74 < self.mark_100 < 90:
                result = True

            elif self.mark == 3 and 59 < self.mark_100 < 75:
                result = True

            elif self.mark == 2 and 34 < self.mark_100 < 60:
                result = True

            elif self.mark == 1 and 0 < self.mark_100 < 35:
                result = True
            elif self.mark == 0 and self.mark_100 == 0:
                result = True

            return result
