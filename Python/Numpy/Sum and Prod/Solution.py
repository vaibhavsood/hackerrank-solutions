import numpy
n, m = list(map(int, input().split()))
#nums = [row [list(map(int, input().split()))]]
arr = numpy.array([input().split() for _ in range(n)], int)
arr = numpy.sum(arr, axis = 0)
print(numpy.prod(arr, axis = None))
