from app.utilities.lists import csv_func, push
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
            csv_func(src, lambda row: self.add(row))
        else:
            src = src if src else []
            for _, row in enumerate(src):
                self.add(row)

    def add(self, data):
        """
        Add a row to data. Calls add() to  update the cols with new values.
        """
        if not self.cols:
            self.cols = Cols(data)
        else:
            row = []
            if data is not None:
                row = push(self.rows, data.cells)
            else:
                row = push(self.rows, Row(data))
            for _, todo in enumerate(self.cols.x, self.cols.y):
                for _, col in enumerate(todo):
                    col.add(row.cells[col.at])

    def stats(self, showCols, func, places = 2):
        showCols = showCols if showCols is not None else self.cols.y
        # func = func if func is not None else Num.mid
        t = {}
        for _, col in enumerate(showCols):
            v = func(col)
            v = rnd(v, places) if isinstance(v, int) else v
            t[col.name] = v
        return t