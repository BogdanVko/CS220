import sys

''' provided
    strings are immutable, but lists are mutable 
    replace(s,i,c) turns string s into a list, replaces s[i] with c,
    then turns the list back into a string and returns it
'''


def replace(s, i, c):
    s = list(s)
    s[i] = c
    s = ''.join(s)
    return s


'''
    return a string with n c-s
'''


def stringn(n, c):
    return n * c


'''
  given bit string bs of size n, 
  return the next (boolean increment)
  e.g.  '00000' -> '00001'
        '01011' -> '01100'
        '11111' -> '00000' 
'''


def next(bs, n):
    return '{:0{}b}'.format(int(bs, 2) + 1, n)[-n:]


'''
   return the set of all length n>=2 bitstrings 
   that start with '11' or end with '1'
'''


def binary_to_decimal(binary):
    binary = int(binary)
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def s11x1(n):

    range_lim = bin(1).replace("0b", "")
    for i in range(0, n - 1):
        range_lim += bin(1).replace("0b", "")

    #print(range_lim)

    range_lim = binary_to_decimal(range_lim)  # decimal of that binary value
    #print(range_lim)  # end point works
    ret_set = []

    for i in range(0, range_lim + 1):
        mask_first_two = 3
        mask_first_one = 1
        if (i & mask_first_one) == 1:
            binary_string = decimal_to_binary(i)
            if len(binary_string) < n - 1:
                binary_string = '0' * (n - len(binary_string)) + binary_string
            ret_set.append(binary_string)

    for i in range(0, range_lim + 1):
        mask_first_two = 3
        mask_first_one = 1
        if (i >> (n - 2) & mask_first_two) == 3:
            binary_string = decimal_to_binary(i)
            ret_set.append(binary_string)

    return set(ret_set)


'''
   return the set of all length n>=2 bitstrings
   that start with '11'
'''


def s11x(n):
    range_lim = bin(1).replace("0b", "")
    for i in range(0, n - 1):
        range_lim += bin(1).replace("0b", "")

    #print(range_lim)

    range_lim = binary_to_decimal(range_lim)  # decimal of that binary value
    #print(range_lim)  # end point works
    ret_set = []
    for i in range(0, range_lim + 1):
        mask_first_two = 3
        mask_first_one = 1
        if (i >> (n - 2) & mask_first_two) == 3:
            binary_string = decimal_to_binary(i)
            ret_set.append(binary_string)

    return set(ret_set)


'''
   return the set of all length n>=2 bitstrings 
   that end with '1'
'''


def sx1(n):
    range_lim = bin(1).replace("0b", "")
    for i in range(0, n - 1):
        range_lim += bin(1).replace("0b", "")

    #print(range_lim)

    range_lim = binary_to_decimal(range_lim)  # decimal of that binary value
    #print(range_lim)  # end point works
    ret_set = []
    for i in range(0, range_lim + 1):
        mask_first_two = 3
        mask_first_one = 1
        if (i & mask_first_one) == 1:
            binary_string = decimal_to_binary(i)
            if len(binary_string) < n-1:
                binary_string = '0'*(n-len(binary_string)) + binary_string
            ret_set.append(binary_string)

    return set(ret_set)


if __name__ == "__main__":
    # sets of bit strings size n
    n = int(2)
    if n < 2:
        print('argument must be >= 2')
        sys.exit()
    s3 = s11x1(n)
    print("s3 = ", s11x1(n))
    print('len(s3) =', len(s3))
    s2 = s11x(n)
    print('len(s2) =', len(s2))
    s1 = sx1(n)
    print('len(s1) =', len(s1))
    print('len(s1&s2):', len(s1 & s2))
    print('s3 == s2|s1:', s3 == s2 | s1)
    print('len(s3) == len(s2)+len(s1)-len(s2&s1):',
          len(s3) == len(s2) + len(s1) - len(s2 & s1))
