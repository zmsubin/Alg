import binary
def is_palindrome(num, base):
    if base == 10:
       numstr = str(num)
    elif base == 2:
       numstr = str(binary.num_to_bin(num))
    else:
       raise Exception('Unsupported')
    return numstr== numstr[::-1]
    
