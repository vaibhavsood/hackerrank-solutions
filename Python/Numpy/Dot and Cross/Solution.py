import numpy
n = int(input())
arr1 = numpy.array([input().split() for _ in range(n)], int)
arr2 = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(arr1, arr2))
