import itertools

from app.utilities.lists import csv_func, push
from app.utilities.misc import obj, rnd
from app.objects.row import Row
from app.objects.cols import Cols


class Data(obj):
    """
    Data is a holder of 'rows' and their summaries (in 'cols')
    """
    def __init__(self, src):
        """
        :param src:
        """
        super().__init__()
        self.cols = None                            # summaries of data
        self.rows = []                              # kept data
        if isinstance(src, str):
            csv_func(src, lambda row: self.add(row))
        else:
            src = src if src else []
            for _, row in enumerate(src):
                self.add(row)

    def add(self, data):
        """Add a row to data. Calls add() to  update the cols with new values.
        :param data: a single Row entry
        :return: None
        """
        if not self.cols:
            self.cols = Cols(data)
        else:
            row = push(self.rows, data if isinstance(data, Row) else Row(data))
            for col in itertools.chain(self.cols.x, self.cols.y):
                col.add(row.cells[col.at])

    def stats(self, places, showCols, func):
        showCols = showCols if showCols is not None else self.cols.y
        t = {}
        for col in showCols:
            v = func(col)
            v = rnd(v, places) if isinstance(v, int) else v
            t[col.name] = v
        return t
