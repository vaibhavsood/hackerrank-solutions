import numpy
res = []
n, m = input().split()
for _ in range(int(n)):
   res.append(list(map(int,input().split(' ')))) 
arr = numpy.array(res)
print(numpy.transpose(arr))
print(arr.flatten())