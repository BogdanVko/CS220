import sys


def invariant(n, k, e, left, right):
    return e*(n**k) == left**right

def eExp(left, right):
    # precondition: left>0 AND right>0
    if left <= 0 or right <= 0: raise "eExp: invalid inputs!"
    n = left
    k = right
    e = 1  # e: the exponent
    assert invariant(n, k, e, left, right)  # fill in the proper loop invariant
    while (k != 0):  # the loop test
        assert True and invariant(n, k, e, left, right)  # fill in the proper loop test and loop invariant
        print("   n:", n, "k:", k, "e:", e)
        # body
        if k % 2 == 1:
            e = e * n
        n = n ** 2
        k = k // 2
        assert invariant(n, k, e, left, right)  # fill in the proper loop invariant
    print("k:", k, "e:", e)
    assert True and invariant(n, k, e, left, right)  # fill in proper not(loop test) and loop invariant
    return e


if __name__ == "__main__":
    print("program:", sys.argv[0], sys.argv[1], sys.argv[2])
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    e = eExp(n, k)
    print(n, "**", k, "=", e)
