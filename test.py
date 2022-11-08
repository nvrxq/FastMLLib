from LinAlgLib.array.TensorS import Tensor, TensorList

a = TensorList([24,123,2424])
print(f'Shape a : {a.view()}')

b = Tensor([[23,21],[223,242]])
print(f'Shape b : {b.view()}')
