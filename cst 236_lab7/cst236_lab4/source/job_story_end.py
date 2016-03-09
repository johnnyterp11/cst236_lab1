import time
from decimal import *
from datetime import datetime
import random
import math

getcontext().prec = 5


def check_n_pi(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1) ** k / (1024 ** k)) * (
            Decimal(256) / (10 * k + 1) + Decimal(1) / (10 * k + 9) - Decimal(64) / (10 * k + 3) - Decimal(32) / (
                4 * k + 1) - Decimal(4) / (10 * k + 5) - Decimal(4) / (10 * k + 7) - Decimal(1) / (4 * k + 3))
        k += 1
    pi = pi * 1 / (2 ** 6)
    return pi


def fiboncci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboncci_number(n - 1) + fiboncci_number(n - 2)


def check_current_time():
    return time.strftime("%c")


def conversion_func(num=0.0, unit_1='', unit_2=''):
    def fract(a=''):
        if a == 'cm':
            return 10.0
        if a == 'm':
            return 1000.0
        if a == 'mm':
            return 1.0
        if a == 'km':
            return 10000000.0
        if a == 'in':
            return 25.4
        if a == 'ft':
            return 304.8
        if a == 'yd':
            return 914.4
        if a == 'mi':
            return 1609344.0

    return num * fract(unit_1) / fract(unit_2)


def ten_conversions(num=0.0, unit_1='', unit_2='', unit_3='', unit_4='', unit_5='', unit_6='', unit_7='', unit_8='',
                    unit_9='', unit_10=''):
    def fract(a=''):
        if a == 'cm':
            return 10.0
        if a == 'm':
            return 1000.0
        if a == 'mm':
            return 1.0
        if a == 'km':
            return 10000000.0
        if a == 'in':
            return 25.4
        if a == 'ft':
            return 304.8
        if a == 'yd':
            return 914.4
        if a == 'mi':
            return 1609344.0
        if a == 'micron':
            return 0.0001
        if a == 'micrometer':
            return 0.000001

    return [num * fract(unit_1) / fract(unit_2), num * fract(unit_3) / fract(unit_4),
            num * fract(unit_5) / fract(unit_6),
            num * fract(unit_7) / fract(unit_8), num * fract(unit_9) / fract(unit_10)]


def ask_user(user):
    string = "I m afraid I can not do that"
    print (string, user)


def check_legal_age_to_drive(age):
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
    if not isinstance(num,(int,float)):
        return 'invalid'
    r = 180 / math.pi
    return num * r


def event_calender(month):
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


def cube(x):
    if not isinstance(x, (int, float)):
        return "invalid"
    else:
        return x * x * x
