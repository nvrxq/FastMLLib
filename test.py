from LinAlgLib.array.TensorS import Tensor, TensorList

a = TensorList([24,123,2424])
print(a[2])


b = Tensor([[1,2,3],[4,5,6]])
print(b.T()[0])