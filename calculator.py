import numpy as np

a = np.arange(15).reshape(3, 5)

print a
print a.shape
print a.ndim
print a.dtype.name
print a.itemsize
# 8
print a.size
# 15
print type(a)
# <type 'numpy.ndarray'>
b = np.array([6, 7, 8])
print b
# array([6, 7, 8])
print type(b)
# <type 'numpy.ndarray'>