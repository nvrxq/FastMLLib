import LinAlgLib_C
from utils import (
    mean
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

    def __repr__(self) -> str:
        return f"FastLinAlg.TensorList:{self.array}"

    def __len__(self):
        return len(self.array)

    def view(self):
        return (self._paramR, self._paramC)

    def __getitem__(self, column, rows=None):
        if rows is None:
            return self.array[column]
        else:
            return self.array[column][rows]

    def dot(self, object1):
        # return LinAlgLib_C.Dot(self.array, object2.array)
        if self._paramC != object1._paramC:
            return 0

        return sum(i[0] * i[1] for i in zip(self.array, object1.array))

    def sum(self):
        return sum(self.array)

    def mean(self, axis=0):
        return TensorList(mean(self, axis=axis))

    # Overload

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

    def __radd__(self, other):
        return TensorList([float(item + other) for item in self.array])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__imul__(other)

        if self._paramR != len(other):
            raise IndexError("Tensors must be similar shape!")
        return TensorList(LinAlgLib_C.Dot(self.array, other.array))

    def __imul__(self, other):
        return TensorList([float(item * other) for item in self.array])

    def median(self):
        med = 0
        if self._paramR % 2 == 0:
            for i in self.array:
                med += i
            return med/self._paramR
        else:
            return list(sorted(self.array))[int(self._paramR/2)]

    def bincount(self):
        result = []
        buff = []
        
        for i in self.array:
            count = 0
            if i not in buff:
                buff.append(i)
                for j in self.array:
                    if i == j:
                        count+=1
                result.append(count)

        return result
    


    def argmax(self):
        value, index = max([(v,i) for i,v in enumerate(self.array)])
        return index



    def log(self):
        result = []

        for i in self.array:
            result.append(1000.0 * ((i ** (1/1000.0)) - 1))

        return result
    


    def accuracy(output, y):
        hit = 0
        output = self.argmax(output, axis=1)
        y = self.argmax(y, axis=1)
        for y in zip(output, y):
            if(y[0]==y[1]):
                hit += 1

        p = (hit*100)/output.shape[0]
        return p
    


    def ReLu(x, derivative=False):
        if(derivative==False):
            return x*(x > 0)

        else:
            return 1*(x > 0)



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
    print(test2.mean())
