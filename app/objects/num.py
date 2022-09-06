import math
import random


class Num:
    def __init__(self, c: int = 0, s: str = ""):
        """
        Summarizes a stream of numbers
        """
        self.n = 0                                  # items seen
        self.at = c                                 # column position
        self.name = s                               # column name
        self.has = []                               # kept data
        self.lo = -math.inf                         # lowest seen
        self.high = math.inf                        # highest seen
        self.isSorted = True                        # no updates since last sort of data
        # check if ending with '-', return -1 if true, 1 otherwise
        self.w = -1 if s.endswith("-") else 1
        self.the = {"nums": 512}

    def nums(self):
        if not self.isSorted:
            # sort the data first
            self.has = sorted(self.has)
            # mark the isSorted flag true after sorting
            self.isSorted = True
        return self.has

    def add(self, v):
        if v != "?":
            self.n = self.n + 1
            self.lo = v if v < self.lo else self.lo
            self.high = v if v > self.high else self.high
            if len(self.has) < self.the["nums"]:
                self.isSorted = False
                self.has.append(int(v))
            elif random.randint(0, self.the["nums"]) < self.the["nums"]/self.n:
                self.isSorted = False
                pos = random.randint(0, len(self.has))
                self.has[pos] = int(v)

    def mid(self):
        array = self.nums()
        return len(array)//2

