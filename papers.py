#!/usr/bin/env python3

""" Computer-based immigration office for Kanadia """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import re
import datetime
import json


def decide(input_file, watchlist_file, countries_file):

    #the following with statements read the files defined in the functions parameters
    with open(input_file, 'r') as file_reader:
        input_contents = input_file.read()
        entries_contents = json.loads(input_contents)

    with open(watchlist_file, 'r') as watchlist_file:
        watchlist_file_contents = watchlist_file.read()
        watchlist_contents = json.loads(watchlist_file_contents)

    with open(countries_file, 'r') as countries_file:
        countries_file_contents = countries_file.read()
        countries_contents = json.loads(countries_file_contents)

    #the for loops will check for all the available items in the aforementioned files
    for entry in entries_contents:
        entry_passport = entry_passport['passport']
        entry_last_name = entry_last_name ['last_name']
        entry_reason = entry_reason ['entry_reason']
        for watchlist_entry in watchlist_contents:
            watchlist_entry = watchlist_entry ['passport']



            for country_entry in countries_contents:
                country_entry




            
"""

    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param watchlist_file: The name of a JSON formatted file that contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether
        an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are: "Accept", "Reject", "Secondary", and "Quarantine"

    """


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :rtype : object
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    passport_format = re.compile('.{5}-.{5}-.{5}-.{5}-.{5}')

    if passport_format.match(passport_number):
        return True
    else:
        return False


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
