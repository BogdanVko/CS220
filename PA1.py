"""
     PA1: Boolean functions and truth-table inputs
     -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

For PA1 you will implememnt a number of Boolean functions,
such as implies, nand, etc.

a) Boolean functions
You are provided with a set of undefined functions.You will
create the bodies for these 2 parameter functions, such that
they return the appropriate Boolean value (True or False).
The formal parameters are always p and q (in that order)

Notice the difference between npIMPnq and nqIMPnp:
In npIMPnq you return not p implies not q (not first
param implies not second param), for example
  npIMPnq(True,False) returns True.

In nqIMPnp you return not q implies not p (not second
param implies not first param), for example
  nqIMPnp(True,False) returns False.

b) Truth-table inputs
The function make_tt_ins(n) will create a truth table for
all combinations of n Boolean variables. A truth table is
an arrayList of 2**n arrayLists of n Booleans. For example
  make_tt_ins(2) returns
[[False, False], [False, True], [True, False], [True, True]]

Notice the recursive nature of make_tt_ins(n):
 It consists of a truth-table(n-1), each row prefixed with False
 followed by the same truth-table(n-1), each row prefixed with True,
 with a base case for n==1: [[False], [True]]

Two functions are provided: run(f) and main, so that you can test
your code.

  python3 PA1.py <fName> tests your Boolean function <fName>
  python3 PA1.p=y tt <n> tests your function make_tt_ins(<n>)

"""

import sys


# p implies q
def implies(p, q):
    if p == True and q == False:
        return False
    return True


# not p implies not q
def npIMPnq(p, q):
    return implies(not p, not q)


# not q implies not p
def nqIMPnp(p, q):
    return implies(not q, not p)


# p if and only if q: (p implies q) and (q implies p)
def iff(p, q):
    return implies(p, q) and implies(q, p)


# not ( p and q )
def nand(p, q):
    return not (p and q)


# not p and not q
def npANDnq(p, q):
    return (not p) and (not q)


# not ( p or q)
def nor(p, q):
    return not (p or q)


# not p or not q
def npORnq(p, q):
    return (not p) or (not q)


def make_tt_ins(n):
    if n < 1:
        return [[]]

    table = make_tt_ins(n - 1)

    return [i + [j] for i in table for j in [False, True]]


# provided
def run(f):
    print("  True,True  : ", f(True, True))
    print("  True,False : ", f(True, False))
    print("  False,True : ", f(False, True))
    print("  False,False: ", f(False, False))
    print()


# provided
if __name__ == "__main__":
    print("program", sys.argv[0])
    f1 = sys.argv[1]
    print(f1);
    if (f1 == "implies"):
        run(implies);
    if (f1 == "iff"):
        run(iff)
    if (f1 == "npIMPnq"):
        run(npIMPnq)
    if (f1 == "nqIMPnp"):
        run(nqIMPnp)
    if (f1 == "nand"):
        run(nand)
    if (f1 == "nor"):
        run(nor)
    if (f1 == "npANDnq"):
        run(npANDnq)
    if (f1 == "npORnq"):
        run(npORnq)
    if (f1 == "tt"):
        print(make_tt_ins(int(sys.argv[2])))

