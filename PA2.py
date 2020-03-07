'''
          PA2: Truth tables and equivalence
          -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

For PA2 you will be provided with a function callf2(f,p,q)
which will cal f(p,q), and with a main to test your code.
You will implement two functions: eval_tt_f2(f) and
equivalent(tt1,tt2). Read main to understand how the
command line for PA2.py.

The function eval_tt_f2(f) will, given a two argument Boolean
function f ( one of the functions you created in PA1.py), return
the truth table for f. Use your make_tt_ins(n) function from
PA1.py to create an arrayList with n inputs, then use callf2
to append the truth value for f to each row of that arrayList.
For example, eval_tt_f2(iff) will return:

[[False, False, True], [False, True, False], [True, False, False], [True, True, True]]

The function equivalent(tt1,tt2) will return True if tt1 and tt2
are equivalent and False otherwise. For example,
  equivalent(eval_tt_f2(PA1.implies), eval_tt_f2(PA1.nqIMPnp))
will return True.

'''

import sys
import PA1


# provided


def callf2(f, p, q):
    return f(p, q)


# implement this
def eval_tt_f2(f):
    og_list = PA1.make_tt_ins(2)
    for row in og_list:
        row.append(callf2(f, row[0], row[1]))

    return og_list


# implement this
def equivalent(tt1, tt2):



    return tt1 == tt2



# provided
if __name__ == "__main__":
    print("program", sys.argv[0])
    f1 = sys.argv[1]
    argc = len(sys.argv)
    print(f1)
    tt1 = []
    if (f1 == "implies"): tt1 = eval_tt_f2(PA1.implies)
    if (f1 == "iff"): tt1 = eval_tt_f2(PA1.iff)
    if (f1 == "npIMPnq"): tt1 = eval_tt_f2(PA1.npIMPnq)
    if (f1 == "nqIMPnp"): tt1 = eval_tt_f2(PA1.nqIMPnp)
    if (f1 == "nand"): tt1 = eval_tt_f2(PA1.nand)
    if (f1 == "nor"): tt1 = eval_tt_f2(PA1.nor)
    if (f1 == "npANDnq"): tt1 = eval_tt_f2(PA1.npANDnq)
    if (f1 == "npORnq"): tt1 = eval_tt_f2(PA1.npORnq)
    print(tt1)


    if (argc > 2):
        f2 = sys.argv[2]
        print(f2)
        tt2 = []
        if (f2 == "implies"): tt2 = eval_tt_f2(PA1.implies)
        if (f2 == "iff"): tt2 = eval_tt_f2(PA1.iff)
        if (f2 == "npIMPnq"): tt2 = eval_tt_f2(PA1.npIMPnq)
        if (f2 == "nqIMPnp"): tt2 = eval_tt_f2(PA1.nqIMPnp)
        if (f2 == "nand"): tt2 = eval_tt_f2(PA1.nand)
        if (f2 == "nor"): tt2 = eval_tt_f2(PA1.nor)
        if (f2 == "npANDnq"): tt2 = eval_tt_f2(PA1.npANDnq)
        if (f2 == "npORnq"): tt2 = eval_tt_f2(PA1.npORnq)
        print(tt2)
        if equivalent(tt1, tt2):
            print("equivalent!")
        else:
            print("NOT equivalent!")
    print()

#  print(equivalent(eval_tt_f2(PA1.implies), eval_tt_f2(PA1.nqIMPnp)))
