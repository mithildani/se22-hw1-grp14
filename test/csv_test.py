from app.utilities.lists import csv_func
from app.utilities.strings import oo


def csv_test():
    def row(t, n):
        n = n+1
        if n > 10:
            return
        else:
            oo(t)
    n = 0
    csv_func("data\\test_file.txt", lambda t, n=n: row(t, n))
    return True
