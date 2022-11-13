from LinAlgLib.array.TensorS import *
import time 
import numpy as np
a = [float(i) for i in range(10000000)]
b = TensorList(a)


start_time = time.time()
c = b.Dot(b)
print("--- %s seconds --- LinAlgLib" % (time.time() - start_time))


def dotd(a,b):
    sol = []
    for i in range(len(a)):
        sol.append(a[i] * b[i])
    return sol


start_time = time.time()
p = dotd(a,a)
print("--- %s seconds --- Python" % (time.time() - start_time))


start_time = time.time()
g = [a[i] * a[i] for i in range(len(a))]
print("--- %s seconds --- Python Generator" % (time.time() - start_time))


start_time = time.time()
n = np.array(a) * np.array(a)
print("--- %s seconds --- Numpy" % (time.time() - start_time))
