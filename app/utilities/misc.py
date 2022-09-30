import math

# TODO rogues
# def rogues():
#   for k,v in ENV.items():
#     if not b4[k]:
#       print("?", k, type(v))


def rnd(x, places):
    if not places:
        mult = 10**2
    else:
        mult = 10**places
    return math.floor(x*mult+0.5) / mult


class obj:
    def __init__(self):
        self.classname = self.__class__.__name__

    def __str__(self):
        return self.classname   # TODO +o(x)



  



