import time
from decimal import *

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
    return time.strftime("%a,%b");