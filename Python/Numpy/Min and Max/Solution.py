import numpy
n, m = list(map(int, input().split()))
arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.max(numpy.min(arr, axis = 1)))
