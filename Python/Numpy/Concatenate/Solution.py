import numpy
n, m, p = list(map(int, input().split()))
mat1 = []
mat2 = []
for _ in range(n):
    mat1.append(list(map(int, input().split())))
for _ in range(m):
    mat2.append(list(map(int, input().split())))
print(numpy.concatenate((mat1, mat2), axis = 0))    
