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

class eg(obj):

    def __init__(self, c: int = 0, s: str = ""):
        super().__init__()
        self.fails = 0

    def runs(k):
        if k not in eg.LIST():
            return
        random.seed(the["seed"])  # reset seed [1]
        old = {}
        for i, v in the.item():
            old[i] = v  # [2]

        if the["dump"]:  # [4]
            status, out = True, eg.LIST()[k]()
        else:
            try:
                out = eg.LIST()[k]
                status = True
            except:
                out = "Error"
                status = False

        for i, v in old.item():
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
        t = []
        lis = [eg.ALL, eg.BAD, eg.bignum, eg.csv, eg.data, eg.LIST, eg.LS,
               eg.num, eg.stats, eg.sym, eg.the]            # list of all functions in class eg

        sort_lis = t.sort()
        # method_list = [method for method in dir(
        #     eg) if method.startswith('__') is False]

        for k in lis:
            t.append(k)
        return t

    # List test names.
    def LS():
        print("\nExamples lua csv -e ...")
        for k in eg.LIST():
            print(str(k).split()[2][3:])
        return True

    # Run all tests
    def ALL():
        for k in eg.LIST():
            if str(k).split()[2][3:] != "ALL":
                print("\n-----------------------------------")
            if not eg.runs(k):
                fails = fails + 1
        return True

    

    def test_bignum():
        num=Num()
        #   the.nums = 32
        for i in range(1,1000):
            num.add(i)
        oo(num.nums())
        return 32==len(num.has)

    def test_sym():
        sym=Sym()

        for x in ["a","a","a","a","b","b","c"]:
            sym.add(x)

        mode, entropy = sym.mid(), sym.div()
        entropy = (1000*entropy)//1/1000            #?
        oo({'mid':mode, 'div':entropy})
        return mode=="a" and 1.37 <= entropy and entropy <=1.38

        
    def test_num():
        num=Num()
        for i in range(1,100):
            num.add(i)
        mid,div = num.mid(), num.div()
        print(mid ,div)
        return 50<= mid and mid<= 52 and 30.5 <div and div<32

        
    def test_stats():
        
        def div(column):
            return column.div()
        def mid(column):
            return column.mid()

        data = Data("data\\test_file.txt")
        
        print("xmid", o(data.stats(2,data.cols.x, mid)))
        print("xdiv", o(data.stats(3,data.cols.x, div)))
        print("ymid", o(data.stats(2,data.cols.y, mid)))
        print("ydiv", o(data.stats(3,data.cols.y, div)))
        
        return True
    
    
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


    def test_the():
        oo(the)
        return True



