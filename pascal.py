import sys
sys.setrecursionlimit(2001)

def pascal(num):
    if num < 1:
        raise(RuntimeError)
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        array = [1]*num
        pascal_minus1 = pascal(num-1)
        for i in range(1,num-1):
            array[i] = pascal_minus1[i-1] + pascal_minus1[i]
        return array

def pascal_iterative(num):
    if num < 1:
        raise(RuntimeError)
    arrayout = [[1]]
    if num == 1:
        return arrayout
    arrayout.append([1, 1])
    if num == 2:
        return arrayout
    for i in range(3, num+1):
        row = [1]*(i)
        for j in range(1, i-1):
            #print i
            #print j
            row[j] = arrayout[i-2][j-1] + arrayout[i-2][j]
        arrayout.append(row)
    return arrayout


if __name__ == '__main__':
    #num = int(input("Number for Pascal row\n"))
    #while num > 0:
    #    print pascal_iterative(num)
    #    num = int(input("Number for Pascal row\n"))
    array = pascal(2000)

