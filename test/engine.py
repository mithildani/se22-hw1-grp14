# -- ## Test Engine
# local eg, fails = {},0

# -- 1. reset random number seed before running something.
# -- 2. Cache the detaults settings, and...
# -- 3. ... restore them after the test
# -- 4. Print error messages or stack dumps as required.
# -- 5. Return true if this all went well.

from app.utilities.settings import the
import random
from app.utilities.misc import obj
from app.objects.num import Num
from app.utilities.strings import oo
from app.utilities.strings import o
from app.utilities.lists import csv_func
from app.objects.data import Data
from app.utilities.lists import csv
from app.objects.sym import Sym
import collections


class eg(obj):

    def __init__(self):
        super().__init__()
        self.fails = 0

    def runs(k):
        if k not in eg.LIST().values():
            return
        random.seed(the["seed"])  # reset seed [1]
        old = {}
        for i, v in the.items():
            old[i] = v  # [2]

        if the["dump"]:  # [4]
            status, out = True, k()
        else:
            try:
                out = k()
                status = True
            except:
                out = False
                status = False

        for i, v in old.items():
            the[i] = v  # restore old settings [3]

        if status:
            if out:
                msg = "PASS"
            else:
                msg = "FAIL"
        else:
            msg = "CRASH"  # [4]
        print("!!!!!!", msg, k, status)
        return out

    # Test that the test happens when something crashes?

    def BAD():
        print(eg.dont.have.this.field)

    # Sort all test names.
    def LIST():
        lis = {"ALL": eg.ALL, "bignum": eg.bignum, "csv": eg.csv, "data": eg.data, "LIST": eg.LIST, "LS": eg.LS,
               "num": eg.num, "stats": eg.stats, "sym": eg.sym, "the": eg.the}            # list of all functions in class eg

        sort_lis = collections.OrderedDict(lis)
        # method_list = [method for method in dir(
        #     eg) if method.startswith('__') is False]
        return sort_lis

    # List test names.
    def LS():
        print("\nExamples lua csv -e ...")
        for i, k in eg.LIST().items():
            print(i)
        return True

    # Run all tests
    def ALL(self):
        for i, k in eg.LIST().items():
            if i != "ALL":
                print(i)
                print("\n-----------------------------------")
                if not eg.runs(k):
                    self.fails = self.fails + 1
        return True

    def bignum():
        num = Num()
        #   the.nums = 32
        for i in range(1, 1000):
            num.add(i)
        oo(num.nums())
        return 999 == len(num.has)

    def sym():
        sym = Sym()

        for x in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(x)

        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000  # ?
        oo({'mid': mode, 'div': entropy})
        return mode == "a" and 1.37 <= entropy and entropy <= 1.38

    def num():
        num = Num()
        for i in range(1, 100):
            num.add(i)
        mid, div = num.mid(), num.div()
        print(mid, div)
        return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

    def stats():

        def div(column):
            return column.div()

        def mid(column):
            return column.mid()

        data = Data("data\\test_file.txt")

        print("xmid", o(data.stats(2, data.cols.x, mid)))
        print("xdiv", o(data.stats(3, data.cols.x, div)))
        print("ymid", o(data.stats(2, data.cols.y, mid)))
        print("ydiv", o(data.stats(3, data.cols.y, div)))

        return True

    def csv():
        def row(t, n):
            n = n+1
            if n > 10:
                return
            else:
                oo(t)
        n = 0
        csv_func("data\\test_file.txt", lambda t, n=n: row(t, n))
        return True

    def the():
        oo(the)
        return True

    def data():
        d = Data("data\\test_file.txt")
        for col in d.cols.y:
            oo(col)
        return True
