import numpy
n, m = list(map(int, input().split()))
numpy.set_printoptions(sign=' ')
print(numpy.eye(n, m, k=0))
