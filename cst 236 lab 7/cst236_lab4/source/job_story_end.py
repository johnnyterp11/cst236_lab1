import time
from decimal import Decimal, getcontext
from datetime import datetime
import math

getcontext().prec = 5


def check_n_pi(number):
    """
    func that return the pi digit
    :param number:
    :return:
    """
    digit = Decimal(0)
    k = 0
    while k < number:
        digit += (Decimal(-1) ** k / (1024 ** k)) * (
            Decimal(256) / (10 * k + 1) + Decimal(1) /
            (10 * k + 9) - Decimal(64) / (10 * k + 3) - Decimal(32) / (
                4 * k + 1) - Decimal(4) / (10 * k + 5) - Decimal(4) /
            (10 * k + 7) - Decimal(1) / (4 * k + 3))
        k += 1
    digit = digit * 1 / (2 ** 6)
    return digit


def fiboncci_number(num):
    """
    func that return fiboncci number
    :param num:
    :return:
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fiboncci_number(num - 1) + fiboncci_number(num - 2)


def check_current_time():
    """
    func that return current time
    :rtype: object
    :return:
    """
    return time.strftime("%c")


def conversion_func(num=0.0, unit_1='', unit_2=''):
    """
    func that returns  unit conversion
    :rtype: object
    :param num:
    :param unit_1:
    :param unit_2:
    """

    def fraction(number=''):
        """

        :param number:
        :rtype: object
        """
        if number == 'cm':
            return 10.0
        if number == 'm':
            return 1000.0
        if number == 'mm':
            return 1.0
        if number == 'km':
            return 10000000.0
        if number == 'in':
            return 25.4
        if number == 'ft':
            return 304.8
        if number == 'yd':
            return 914.4
        if number == 'mi':
            return 1609344.0

    return num * fraction(unit_1) / fraction(unit_2)


def ten_conversions(num=0.0, unit_1='', unit_2='', unit_3='',
                    unit_4='', unit_5='', unit_6='', unit_7='', unit_8='',
                    unit_9='', unit_10=''):
    """
    func that returns  10 units conversion

    :param unit_10:
    :param unit_9:
    :param unit_8:
    :param unit_7:
    :param unit_6:
    :param unit_5:
    :param unit_3:
    :param unit_2:
    :param unit_1:
    :param num:
    :type unit_4: object
    """

    def fraction(value=''):
        """

        :param value:
        :return:
        """
        if value == 'cm':
            return 10.0
        if value == 'm':
            return 1000.0
        if value == 'mm':
            return 1.0
        if value == 'km':
            return 10000000.0
        if value == 'in':
            return 25.4
        if value == 'ft':
            return 304.8
        if value == 'yd':
            return 914.4
        if value == 'mi':
            return 1609344.0
        if value == 'micron':
            return 0.0001
        if value == 'micrometer':
            return 0.000001

    return [num * fraction(unit_1) / fraction(unit_2), num * fraction(unit_3) / fraction(unit_4),
            num * fraction(unit_5) / fraction(unit_6),
            num * fraction(unit_7) / fraction(unit_8), num * fraction(unit_9) / fraction(unit_10)]


def ask_user(user):
    """

    :param user:
    """
    string = "I m afraid I can not do that"
    print (string, user)


def check_legal_age_to_drive(age):
    """

    :param age:
    :return: valid age to drive
    """
    born = datetime.strptime(age, '%Y-%m-%d')
    today = datetime.now()

    if born > today:
        return "invalid"
    else:

        age = today.year - born.year

        if age >= 16:
            return "legal"
        if age < 16:
            return "not legal"


def yellow_book(data):
    """

    :param data:
    :return: valid data in the dict
    """
    info = {
        'Robert': '555-6564612',
        'Joly': '555-7456612'
    }
    if not isinstance(data, basestring):
        return "Invalid"

    for name, number in info.iteritems():
        if name == data:
            return number


def convert_radian_to_degrees(num):
    """

    :param num:
    :return: radian
    """
    if not isinstance(num, (int, float)):
        return 'invalid'
    radian = 180 / math.pi
    return num * radian


def event_calender(month):
    """

    :param month:
    :return: events
    """
    project_data = {
        'January 2010': ' project start',
        'February 2010': ' budget review',
        'March 2010': ' Decision made',
        'April 2010': ' project ends'

    }

    if not isinstance(month, basestring):
        return "invalid"

    for date, event in project_data.iteritems():
        if date == month:
            return event


def cube(num):
    """

    :param num:
    :return: cubic number
    """
    if not isinstance(num, (int, float)):
        return "invalid"
    else:
        return num * num * num
