import numpy
n, m = list(map(int, input().split()))
a = []
for _ in range(n):
    temp = list(map(int, input().split()))
    a.append(temp)
b = []
for _ in range(n):
    temp = list(map(int, input().split()))
    b.append(temp)
a = numpy.array(a)
b = numpy.array(b)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))
