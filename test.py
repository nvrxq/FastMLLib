from FastMLLib.array.TensorS import Tensor
import numpy as np


a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

aT = Tensor(a)
bT = Tensor(b)

aN = np.array(a)
bN = np.array(b)

cT = aT.dot(bT.T())
cN = aN.dot(bN.T)


print(cT)
print('-------')
print(cN)
