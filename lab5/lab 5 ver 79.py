"""
The program was created by Nick Kolomiiets
"""

from sys import argv

from Load import *

import json

import csv


def load_ini(path):
    """
    :param path: path to the settings ini file
    :return: dict of files and their pathes
    """
    print('loading settings file')
    with open(path, 'r') as configfile:
        settings = json.load(configfile)
    if _checking_insides(settings):
        print(f'ini {path}: OK')
    else:
        raise Exception('something wrong with settings file')
    return settings


def _checking_insides(settings):
    """
    :param settings: container of settings
    :return: True if settings contain all needed else False
    """
    output = False
    if 'json' in settings['input'] and 'csv' in settings['input']  and \
        'encoding' in settings['input'] and 'fname' in settings['output'] and 'encoding' in settings['output']:
        output = True

    return output


def process(path):
    """
    :param path: path to the settings ini file
    :doing: load the settings file and start loading ganeral and additional files

    """
    settings = load_ini(path)
    information = load(settings['input']['csv'], settings['input']['json'], settings['input']['encoding'])
    information.output(settings['output']['fname'], settings['output']['encoding'])


def info_about_me():

    """
    print information about me
    """

    print("Nick Kolomiiets, K-12")


def goal_of_the_progtam():

    """
    printing the goal of the program
    """

    print('''Variant № 79 The program was created to processe the results of students taking the exams of the winter session.''')


def main():
    info_about_me()
    goal_of_the_progtam()

    arguments = argv

    if len(arguments) == 2:
        try:
            process(arguments[1])
        except BaseException as e:
            print('***** program aborted *****')
            print(e)
    else:
        print('***** program aborted *****')
        print('Wrong number of arguments')

main()