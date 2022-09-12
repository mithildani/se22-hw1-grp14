""" Lua code
-- ### Lists
local copy,per,push,csv
-- deepcopy
function copy(t,    u)
  if type(t) ~= "table" then return t end
  u={}; for k,v in pairs(t) do u[k] = copy(v) end
  return setmetatable(u,getmetatable(t))  end

"""
# TODO: Write python for above code


import math
import csv
from app.utilities.settings import coerce


def per(t, p=0.5):
    p = math.floor(p * len(t))
    return t[max(1, min(len(t), p))]


def csv_func(fname, fun, n):
    with open(fname, mode='r')as file:
        s = list(csv.reader(file))

    for i in range(len(s)):
        t = []
        for word in s[i]:
            t.append(coerce(word))
        fun(t, n)

def push(t,x):
  t.append(x)
  return x