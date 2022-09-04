import math
class Sym:

    def __init__(self, c: int = 0, s: str = ""):
        """
        `Sym`s summarize a stream of symbols.
        :param c: column position
        :param s: column name
        """
        self.n = 0      # items seen
        self.at = c     # column position
        self.name = s   # column name
        self.has = {}   # kept data

    def add(self, v):
        if v != "?":
            self.n = self.n+1
            self.has[v] = 1+self.has.get(v, 0)
    
    def mid(self):
        most = -1
        mode = None
        for k,v in self.has.items():
            if v > most:
                mode, most = k,v
        return mode

    def div(self):
        def fun(p):
            return p*math.log(p)
        e = 0
        for i,j in self.has.items():
            if j>0:
                e = e - fun(j/self.n)
        return e
