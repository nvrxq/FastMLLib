import LinAlgLib_C

from utils import (
    mean, bincount, log, argmax, median, dot, square,
    summary, division
)
from metrics import (
    accuracy, compute_tp_tn_fn_fp, compute_accuracy, compute_precision, compute_recall, compute_f1_score, compute_sens_spec, MSE, MAE
)
from nn import (
    relu, tanh, sigmoid, forward_activation,
)


class TensorList:


    def __init__(self, _list: list) -> None:
        '''
        TensorList
        _list = 1d Array
        '''
        self.array = _list
        self._paramR = None  # Rows
        self._paramC = None  # Columns
        self.shape()

    def shape(self):
        '''
        Return the shape of an array.
        '''
        self._paramR = len(self.array)
        self._paramC = None if isinstance(
            self.array[0], (int, float)) else len(self.array[0])
        if self._paramC:
            for idx in range(self._paramR):
                if len(self.array[idx]) != self._paramC:
                    self._paramC = None
                    break
        else:
            pass

    def item(self):
        return self.array[0]

    def __str__(self) -> str:
        '''
        Return a string representation
        '''
        return f"{self.array}"

    def __len__(self):
        '''
        Find the length of Tensor data type
        '''
        return len(self.array)

    def view(self):
        '''
        New view of array with the same data.
        '''
        return (self._paramR, self._paramC)

    def __getitem__(self, column, rows=None):
        '''
        Return self[key].
        '''
        if rows is None:
            return self.array[column]
        else:
            return self.array[column][rows]

    def dot(self, object1):
        # return LinAlgLib_C.Dot(self.array, object2.array)
        '''
        Links with utils.py for dot function
        '''
        return dot(self, object1)

    def sum(self):
        '''
        Links with utils.py for sum function
        '''
        if self._paramC is None:
            return TensorList([summary(self.array)])
        return Tensor([summary(item) for item in self.array])

    def mean(self, axis=0):
        '''
        Links with utils.py for mean function
        '''
        return TensorList(mean(self, axis=axis))

    def log(self):
        '''
        Links with utils.py for log function
        '''
        return TensorList(log(self))

    def bincount(self):
        '''
        Links with utils.py for bincount function
        '''
        return TensorList(bincount(self))

    # Overload


    def __truediv__(self, scalar):
        if self._paramC is None:
            return TensorList(division(self.array, scalar))
        return Tensor([division(item, scalar) for item in self.array])


    def __add__(self, other):
        '''
        TensorList + TensorList
        T:
            #write C func
        '''
        if isinstance(other, (int, float)):
            return self.__radd__(other)

        if self._paramR != len(other):
            raise IndexError("Tensors must be similar shape!")

        return TensorList([self.array[i] + other.array[i]
                           for i in range(self._paramR)])

    def squared(self):
        if self._paramC is None:
            return TensorList(square(self))
        return Tensor([square(item) for item in self.array])

    def __radd__(self, other):
        '''
        Add other to self, and return a new masked array.
        '''
        return TensorList([float(item + other) for item in self.array])

    def __mul__(self, other):
        '''
        Returns self*value
        '''
        if isinstance(other, (int, float)):
            return self.__imul__(other)

        if self._paramR != len(other):
            raise IndexError("Tensors must be similar shape!")
        return TensorList(LinAlgLib_C.Dot(self.array, other.array))

    def __imul__(self, other):
        '''
        Returns self*=value.
        '''
        return TensorList([float(item * other) for item in self.array])

    def median(self):
        '''
        Links with utils.py to median function
        '''
        return median(self.array, self.paramR)

    def argmax(self):
        '''
        Links with utils.py to tanh activation function
        '''
        return argmax(self)

    def relu(self, x, derivative=False):
        '''
        Links with nn.py to relu activation function
        '''
        return relu(x, derivative)

    def sigmoid(self, x):
        '''
        Links with nn.py to sigmoid activation function
        '''
        return sigmoid(x)

    def tanh(self, x):
        '''
        Links with nn.py to tanh activation function
        '''
        return (tanh)

    def forward_activation(self, x, activation_function):
        '''
        Links with nn.py to choosing activation function
        '''
        return forward_activation(x, activation_function)

    def accuracy(self, _tensor):
        '''
        Links with metrics.py accuracy from output and true
        '''
        return accuracy(self, _tensor)

    def compute_tp_tn_fn_fp(self, _tensor):
        '''
        Links with metrics.py
        True positive
        False positive
        False negative
        True negative
        '''
        return compute_tp_tn_fn_fp(self, _tensor)

    def compute_accuracy(tp, tn, fn, fp):
        '''
        Linking with metrics.py accuracy from 
        True positive
        False positive
        False negative
        True negative
        '''
        return compute_accuracy(tp, tn, fn, fp)

    def compute_precision(tp, fp):
        '''
        Links with metrics.py precision 
        '''
        return compute_precision(tp, fp)

    def compute_recall(tp, fn):
        '''
        Links with metrics.py Recall 
        '''
        return compute_recall(tp, fn)

    def compute_f1_score(self, _tensor):
        '''
        Links with metrics.py f1 score
        '''
        return compute_f1_score(self, _tensor)

    def compute_sens_spec(tp, tn, fp, fn):
        '''
        Links with metrics.py Sensitivity and Specificity
        '''
        return compute_sens_spec(tp, tn, fp, fn)

    def MSE(self, _tensor):
        '''
        Links with metrics.py mean squared error
        '''
        return MSE(self, _tensor)

    def MAE(self, _tensor):
        '''
        Links with metrics.py mean absolute error
        '''
        return MAE(self, _tensor)


class Tensor(TensorList):

    def __init__(self, _list: list[list]) -> None:
        self.array = _list
        self.shape()

    def T(self):
        result = [[self.array[j][i]
                   for j in range(self._paramR)] for i in range(self._paramC)]
        return Tensor(result)

    def dot(self, object1):
        if self._paramC != object1._paramR:
            raise IndexError(
                "Cannot multiply the two matrices. Incorrect dimensions.")

        C = [[0 for row in range(object1._paramC)]
             for col in range(self._paramR)]

        for i in range(self._paramR):
            for j in range(object1._paramC):
                for k in range(self._paramC):
                    C[i][j] += self.array[i][k] * object1.array[k][j]
        return C

    def flatten(self):
        return [i for j in self.array for i in j]

    def median(self):
        flatten_object = self.flatten()
        med = 0
        if len(flatten_object) % 2 == 0:
            for i in flatten_object:
                med += i
            return med / len(flatten_object)
        else:
            return sorted(flatten_object)[int(len(flatten_object)/2)]

            # median for axises and reshape




if __name__ == "__main__":
    #test = Tensor([[24, 21], [214, 214, 23]])
    test = TensorList([1, 2, 3])
    test2 = Tensor([[1, 2], [3, 4]])
    print(test2.squared().mean(axis = 1))
