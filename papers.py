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
    # Decision holds the result of all screenings
    decision = []
    # the following with statements read the files defined in the functions parameters
    with open(input_file, 'r') as file_reader:
        input_contents = input_file.read()
        entries_contents = json.loads(input_contents)

    with open(watchlist_file, 'r') as watchlist_file:
        watchlist_file_contents = watchlist_file.read()
        watchlist_contents = json.loads(watchlist_file_contents)

    with open(countries_file, 'r') as countries_file:
        countries_file_contents = countries_file.read()
        countries_contents = json.loads(countries_file_contents)

    # the for loops will check for all the available items in the aforementioned files

    for entry in entries_contents:
        entry_passport = entry['passport']
        entry_last_name = entry['last_name']
        home_country = entry['country']

        if (entry_passport == "") or (entry_last_name == "") or (home_country == "KAN"):
            return "Accepted"
        else:
            return "Secondary"

    for watchlist_item in watchlist_contents:
        watchlist_passport = watchlist_item['passport']
        watchlist_last_name = watchlist_item['last name']
        watchlist_first_name = watchlist_item['first name']

        if (watchlist_passport == "") or (watchlist_last_name == "") or (watchlist_first_name == ""):
            return "Rejected"
        else:
            print("secondary")

    for countries_item in countries_contents:
        countries_medical = countries_item ['medical_advisory']
        countries_visitor_visa = countries_item ['visitor_visa_required']
        countries_transit_visa = countries_item ['transit_visa_required']

        if (countries_visitor_visa == 1) or (countries_transit_visa == 1):
            return "Secondary"

        if countries_medical == 1:
            return ["Quarantine"]
        else:
            return ["Secondary"]
    else:
        decision.append ("Accept")

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
