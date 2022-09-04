import math

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
        self.isSorted = true                        # no updates since last sort of data
        self.w = -1 if s.endswith("-") else 1       # check if ending with '-', return -1 if true, 1 otherwise
    
     def nums(self):
        if (!self.isSorted):
            self.has = sorted(self.has.items(), key=lambda x: x[1])     # sort the data first
            self.isSorted = True                                        # mark the isSorted flag true after sorting
        return self.has

    