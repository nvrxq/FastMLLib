from LinAlgLib.array.TensorS import *
import time 
import numpy as np

def dotd(a,b):
    sol = []
    for i in range(len(a)):
        sol.append(a[i] * b[i])
    return sol

def test():
    a = [float(i) for i in range(10000000)]
    b = TensorList(a)


    start_time = time.time()
    c = b.Dot(b)
    print("--- %s seconds --- LinAlgLib" % (time.time() - start_time))





    start_time = time.time()
    p = dotd(a,a)
    print("--- %s seconds --- Python" % (time.time() - start_time))


    start_time = time.time()
    g = [a[i] * a[i] for i in range(len(a))]
    print("--- %s seconds --- Python Generator" % (time.time() - start_time))


    start_time = time.time()
    n = np.array(a) * np.array(a)
    print("--- %s seconds --- Numpy" % (time.time() - start_time))

a = Tensor([[1,2],[3,4],[5,6]])
print(a)
print(a.shape())

b = [[1,2],[1,1,10]]
li = list(i for j in b for i in j)
c = Tensor(b)
print(b,li,c.flatten(),c.median())

p = TensorList([1,2,2])

print(p.median())
