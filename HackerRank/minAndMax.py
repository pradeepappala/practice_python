import numpy

arrayDim = list(map(int, input().split()))
array = [list(map(int, input().split())) for _ in range(int(arrayDim[0]))]
print(numpy.max(numpy.min(array, axis = 1)))
'''
my_array = numpy.array([[2, 5],
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print(numpy.max(my_array, axis = 1))        #Output : [4 7]
print(numpy.max(my_array, axis = None))     #Output : 7
print(numpy.max(my_array))                  #Output : 7
'''
