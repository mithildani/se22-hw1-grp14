import math
import random

the = {}


class Num:
    def __init__(self, c: int = 0, s: str = ""):
        """
        Summarizes a stream of numbers
        """
        self.n = 0                                  # items seen
        self.at = c                                 # column position
        self.name = s                               # column name
        self.has = {}                               # kept data
        self.lo = -math.inf                         # lowest seen
        self.high = math.inf                        # highest seen
        self.isSorted = True                        # no updates since last sort of data
        self.w = -1 if s.endswith("-") else 1       # check if ending with '-', return -1 if true, 1 otherwise
    
    def nums(self):
        if not self.isSorted:
            self.has = sorted(self.has.items(), key=lambda x: x[1])     # sort the data first
            self.isSorted = True                                        # mark the isSorted flag true after sorting
        return self.has

    def add(self, v):
        global the
        pos = None
        if v != "?":
            self.n = self.n + 1
            self.lo = v if v < self.lo else self.lo
            self.high = v if v > self.high else self.high
            if len(self.has) < len(the.nums):
                pos = 1 + len(self.has)
            elif random.randint(0, the.nums) < the.nums/self.n:
                pos = random.randint(0, len(self.has))
            if pos is not None:
                self.isSorted = False
                key = list(self.has.keys())[pos]
                self.has[key] = int(v)

    def mid(self):
        array = self.nums()
        return len(array)//2
