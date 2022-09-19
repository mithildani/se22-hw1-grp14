from app.utilities.lists import push
from app.objects.num import Num
from app.objects.sym import Sym
import re
from app.utilities.misc import obj


class Cols(obj):
    def __init__(self, names):
        """
        -- `Columns` Holds of summaries of columns.
        -- Columns are created once, then may appear in  multiple slots.
        :param names:
        """
        super().__init__()
        self.names = names          # all column names
        self.all = []               # all the columns (including the skipped ones)
        self.klass = None           # the single dependent klass column (if it exists)
        self.x = []                 # independent columns (that are not skipped)
        self.y = []                 # dependent columns (that are not skipped)

        for c, s in self.names:
            # Numerics start with Uppercase.
            col = push(self.all, Sym(c, s) if(re.search(r"^A-Z", s) is None) else Num(c, s))

            if re.search(r":$", s) is None:         # some columns are skipped
                # some cols are goal cols
                push(self.x if(re.search(r"!+-", s) is None) else self.y, col)
                if re.search(r"!$", s) is not None:
                    self.klass = col
