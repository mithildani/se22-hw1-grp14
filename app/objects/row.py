from app.utilities.lists import copy
from app.utilities.misc import obj


class Row(obj):
    def __init__(self, t: dict):
        """
        -- `Row` holds one record
        :param t:
        """
        super().__init__()
        self.cells = t              # one record
        self.cooked = copy(t)       # used if we discretize data
        self.isEvaled = False       # True if y-values evaluated.


