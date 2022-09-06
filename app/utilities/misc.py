""" Lua code
-- ### Misc
local rogues, rnd,  obj
-- Find rogue locals.
function rogues()
  for k,v in pairs(_ENV) do if not b4[k] then print("?",k,type(v)) end end end

-- ### Maths
function rnd(x, places)
  local mult = 10^(places or 2)
  return math.floor(x * mult + 0.5) / mult end

-- obj("Thing") enables a constructor Thing:new() ... and a pretty-printer
-- for Things.
function obj(s,    t,i,new)
  function new(k,...) i=setmetatable({},k);
                      return setmetatable(t.new(i,...) or i,k) end
  t={__tostring = function(x) return s..o(x) end}
  t.__index = t;return setmetatable(t,{__call=new}) end
"""

# TODO: Write Python for above functions
import math

#Todo rogues 
# def rogues():
#   for k,v in ENV.items():
#     if not b4[k]:
#       print("?", k, type(v))

def rnd(x,places):
  if not places:
    mult = 10**2
  else
    mult = 10**places
  return math.floor(x*mult+0.5) / mult

class obj:
  def __init__(self):
    self.classname = self.__class__.__name__

  def __str__(self):
    return self.classname #Todo o(x)



  



