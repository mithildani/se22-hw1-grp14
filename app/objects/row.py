"""
LUA Code
function Row:new(t) return {cells=t,          -- one record
                        cooked=copy(t), -- used if we discretize data
                        isEvaled=false    -- true if y-values evaluated.
                       } end
"""
import copy
from app.utilities.lists import copy

class Row():
    def __init__(self, t:dict):
        self.cells = t
        self.cooked = copy.deepcopy(t)
        self.Evaled = False


