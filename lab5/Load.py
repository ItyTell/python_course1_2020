"""
The program was created by Nick Kolomiiets
"""

import json

import csv

from Builder import *


def load(general_path, additional_path, codding):

    """
    load files

    :param general_path: path to the general file

    :param additional_path:path to the additional file

    :param codding: codding of the files

    :return:
    """
    information = Information()
    load_data(information, general_path, codding)
    dict = load_stat(additional_path, codding)
    if fit(information, dict):
        print('json?=csv: OK')
    else:
        print('json?=csv: UPS')
    return information


def load_data(information, general_path, codding):

    """
    load general file into the object of class Builder


    :param information: object of class Information to save data from general file

    :param general_path: str path to the general file

    :param codding: str  codding of the file default = utf-8

    :return:
    """

    builder = Builder()
    information.clear()

    print('loading general file')
    try:
        with open(general_path, encoding=codding) as file:
            builder.load(file, information)
    except Exception as e:
        information.clear()
        raise e
    print(f'input-csv {general_path}: OK')


def load_stat(additional_path, codding):

    """
    :param additional_path: path to the additional file

    :param codding: codding of the file

    """

    try:
        with open(additional_path, encoding=codding) as jfile:
            print('loading second file')
            data = json.load(jfile)
            print(f'input-json {additional_path}: ОК')
    except:
        raise Exception('Something wrong with loading additional file')
    try:
        return {'5': data["кількість оцінок 'відмінно'"], '3': data["кількість оцінок 'задовільно'"],
                       'all': data['загальна кількість записів']}
    except:
        raise Exception('The additional file does not contain all the nessesary files')


def fit(information, dict):

    """

    :param information: Information
    object where data was saved

    :param dict: dict
    dictionary where statistics is saved

    :return: True if files have right data about each other
             False else
    """

    print('Checking if both files have right information')
    best_mark = 0
    good_mark = 0
    quontity = 0
    for student in information.student_list.values():
        for subject in Student.subject_list.values():
            quontity += 1
            if student in subject.mark_list:
                if subject.mark_list[student] == 5:
                    best_mark += 1
                if subject.mark_list[student] >= 3:
                    good_mark += 1
    return best_mark == dict['5'] and good_mark == dict['3'] and quontity == dict['all']

