import math
import random
from app.utilities.lists import per
from app.code import the
from app.utilities.misc import obj

class Num(obj):
    def __init__(self, c: int = 0, s: str = ""):
        """
        Summarizes a stream of numbers
        """
        super().__init__()
        self.n = 0                                  # items seen
        self.at = c                                 # column position
        self.name = s                               # column name
        self.has = []                               # kept data
        self.lo = -math.inf                         # lowest seen
        self.high = math.inf                        # highest seen
        self.isSorted = True                        # no updates since last sort of data
        # check if ending with '-', return -1 if true, 1 otherwise
        self.w = -1 if s.endswith("-") else 1

    def nums(self):
        """
        Return kept numbers, sorted.
        """
        if not self.isSorted:
            # sort the data first
            self.has = sorted(self.has)
            # mark the isSorted flag true after sorting
            self.isSorted = True
        return self.has

    def add(self, v):
        """
        Reservoir sampler. Keep at most `the.nums` numbers
        (and if we run out of room, delete something old, at random).,
        :param v:
        :return:
        """
        if v != "?":
            v = float(v)
            self.n = self.n + 1
            self.lo = v if v < self.lo else self.lo
            self.high = v if v > self.high else self.high
            if len(self.has) < the["nums"]:
                self.isSorted = False
                self.has.append(int(v))
            elif random.randint(0, the["nums"]) < the["nums"]/self.n:
                self.isSorted = False
                pos = random.randint(0, len(self.has))
                self.has[pos] = int(v)

    def div(self):
        """
        Diversity (standard deviation for Nums, entropy for Syms)
        :return:
        """
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1)) / 2.58

    def mid(self):
        """
        Central tendency (median for Nums, mode for Syms)
        :return:
        """
        return per(self.nums(), 0.5)
