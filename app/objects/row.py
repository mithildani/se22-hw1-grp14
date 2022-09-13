"""
LUA Code
function Row:new(t) return {cells=t,          -- one record
                        cooked=copy(t), -- used if we discretize data
                        isEvaled=false    -- true if y-values evaluated.
                       } end
"""

from app.utilities.lists import copy

class Row():
    def __init__(self, t:dict):
        self.cells = t
        self.cooked = copy(t)
        self.Evaled = False


