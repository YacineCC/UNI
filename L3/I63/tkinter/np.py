import numpy as np


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[0])
print(a)

b = np.zeros(3)
print(b)
print(type(b[0]))


c = np.empty(5)

print(c)
print(type(c[0]))


d = np.arange(3, 17, 5)
print(d)

x = np.ones(2, dtype=np.int64)
print(x)
print(type(x[0]))

a = np.ones([9, 5])
c = np.ones([5, 9])
d = np.matmul(a, c)
print(a)
print(c)

z = np.ones(5)
print(print(np.dot(d,z)))
