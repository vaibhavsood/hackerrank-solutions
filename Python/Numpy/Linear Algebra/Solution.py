import numpy
arr = numpy.array([input().split() for _ in range(int(input()))], float)
print("%0.1f"%numpy.linalg.det(arr))    

