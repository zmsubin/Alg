import addarrays
def calcproduct(array, start, direction, numprod):
    product = array[start[0]][start[1]]
    currentpoint = start
    for n in range(numprod-1):
        currentpoint = addarrays.addarrays(currentpoint, direction)
        product *= array[currentpoint[0]][currentpoint[1]]
    return product

#print calcproduct([[1, 2, 3, 4],[5, 6, 7, 8]], [0, 0], [1, 1], 2)
