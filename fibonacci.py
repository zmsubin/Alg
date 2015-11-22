def fibdigits(n):
    array = fibonacci(n)
    arrayout = []
    currentdigits = 1
    numcurrent = 0
    for n in array:
        digits = countdigits(n)
        if digits > currentdigits:
            arrayout.append([currentdigits, numcurrent])
            numcurrent = 0
            currentdigits = digits
        numcurrent += 1
    return arrayout
        

def firstwithn(n):
    current = 1
    previous = 1
    index = 2
    while countdigits(current) < n:
       temp = current + previous
       previous = current
       current = temp
       index += 1
    
    return index






def fibonacci(n):
    array = [];
    if n == 1:
       array = [1]
    elif n == 2:
       array = [1, 1]
    else:
       array = [1, 1]
       for i in range(n-2):
           array.append(array[-1]+array[-2])

    return array


def countdigits(n):
    count = 0
    while n > 0:
       count += 1
       n /= 10

    return count


