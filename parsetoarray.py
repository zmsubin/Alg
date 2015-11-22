def parsetoarray(filename):
    file = open(filename, 'r')
    arrayout = []
    for line in file:
        numbers = line.split(" ")
        numbers = map(lambda num: int(num), numbers)
        arrayout.append(numbers)
    return zip(*arrayout)

#print parsetoarray("numbers.txt")
