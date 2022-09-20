import csv
import math
from copy import deepcopy
from app.utilities.settings import coerce


def copy(t):
    if type(t) is not dict:
        return t
    t_copy = deepcopy(t)
    return t_copy


def per(t, p=0.5):
    p = math.floor(p * len(t))
    return t[max(1, min(len(t), p))]


def csv_func(fname, fun):
    # TODO: Rename function, read without using csv library
    with open(fname, mode='r')as file:
        s = list(csv.reader(file))

    for i in range(len(s)):
        t = []
        for word in s[i]:
            t.append(coerce(word))
        fun(t)


# assuming t is a list
def push(t, x):
    t.append(x)
    return x
