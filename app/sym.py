

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
            self.has[v] = 1+(self.has[v] or 0)
