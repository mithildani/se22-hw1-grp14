from app.utilities.lists import csv, push
from app.utilities.misc import obj, rnd
from app.objects import Cols, Row, Num

class Data(obj):
    def __init__(self, src):
        """
        Data is a holder of 'rows' and their sumamries (in 'cols')
        """
        self.cols = None                            # summaries of data
        self.rows = []                              # kept data
        if (isinstance(src, str)):
            self.addData(self, csv(src))
        else:
            src = src if src is not None else []
            for _, row in enumerate(src):
                self.addData(row)

    def addData(self, data):
        """
        Add a row to data. Calls add() to  update the cols with new values.
        """
        if self.cols is not None:
            self.cols = Cols(data)
        else:
            row = []
            if data is not None and data.cells is not None:
                row = push(self.rows, data.cells)
            elif data is not None and data.cells is None:
                row = push(self.rows, data)
            else:
                row = push(self.rows, Row(data))
            for _, todo in enumerate(self.cols.x, self.cols.y):
                for _, col in enumerate(todo):
                    Cols.addCol(row.cells[col.at])

def stats(self, showCols, func, places = 2):
    showCols = showCols if showCols is not None else self.cols.y
    func = func if func is not None else Num.mid
    t = {}
    for _, col in enumerate(showCols):
        v = func(col)
        v = rnd(v, places) if isinstance(v, int) else v
        t[col.name] = v
    return t