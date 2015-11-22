import calcproduct, parsetoarray

def findmax(numbersfile, numprod):
    arrayin = parsetoarray.parsetoarray(numbersfile)

    max = 0

    for directions in [[0, 1], [1, 0], [1, 1], [-1, 1]]:
        for starty in range(len(arrayin)):
            for startx in range(len(arrayin[0])):
                currentstart = [starty, startx]
                if ((currentstart[0] > len(arrayin) - numprod and
                    directions[0] == 1) or
                    (currentstart[1] > len(arrayin[0]) - numprod and 
                    directions[1] == 1) or
                    (currentstart[0] < numprod -1 and
                    directions[0] == -1)):
                    #(currentstart[1] > len(arrayin[0]) - numprod and
                    #directions[1] == 1)):
                    break
                curprod = calcproduct.calcproduct(arrayin, currentstart, directions, numprod)
                #print ([currentstart[0], currentstart[1]])

                if curprod > max:
                   max = curprod
                   finalstart = currentstart
                   finaldirections = directions

    print "finalstart, directions = "
    print finalstart
    print finaldirections
    return max
