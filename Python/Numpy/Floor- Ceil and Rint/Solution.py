import numpy
nums = list(map(float, input().split()))
numpy.set_printoptions(sign=' ')
nums = numpy.array(nums)
print(numpy.floor(nums))
print(numpy.ceil(nums))
print(numpy.rint(nums))
