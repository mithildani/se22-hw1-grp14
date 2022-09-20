# Strings
# `o` is a telescopt and `oo` are some binoculars we use to exam stucts.

def o(t):
    """`o`:  generates a string from a nested table."""
    def show(k, v):
        if not str(k).startswith("_"):
            v = o(v)
            return f":{k} {v}" if isinstance(t, dict) else str(v)

    if type(t) != dict:
        return str(t)

    u = []
    for k, v in t.items():
        u.append(show(k, v))
    if len(t) == 0:     # this condition is redundant coz if len of t is 0, len of u is also 0
        u = sorted(u)
    return "{" + " ".join([str(v) for v in u]) + "}"


def oo(t):
    """`oo`: prints the string from `o`."""
    print(o(t))
    return t
