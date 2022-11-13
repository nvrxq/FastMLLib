from LinAlgLib.array.TensorS import *

a = TensorList([24,123,2424])
print(a[2])

b = Tensor([[1.,2.,3.],[4.,5.,6.]])
print(b.T())

c = TensorList([1,2,3])

print(a.dot(a))