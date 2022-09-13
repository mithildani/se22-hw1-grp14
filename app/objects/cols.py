from app.utilities.lists import push
from app.objects.num import Num
from app.objects.sym import Sym
import re
from app.utilities.misc import obj


class Cols(obj):
    def __init__(self, names, c: int = 0, s: str = ""):
        self.names = names        # all column names
        # all the columns (including the skipped ones)
        self.all = []
        # the single dependent klass column (if it exists)
        self.klass = None
        self.x = []               # independent columns (that are not skipped)
        self.y = []               # depedent columns (that are not skipped)

        for c, s in obj:
            # Numerics start with Uppercase.
            col = push(self.all, lambda c, s: Sym(c, s) if(
                re.search(r"^A-Z", s) == None) else Num(c, s))

            if re.search(r":$", s) == None:         # some columns are skipped
                # some cols are goal cols
                push(lambda s: self.x if(
                    re.search(r"!+-", s) == None) else self.y, col)
            if re.search(r"!$", s) != None:
                self.klass = col
