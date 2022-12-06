import LinAlgLib_C


class TensorList:
    def __init__(self, _list: list) -> None:
        '''
        TensorList
        _list = 1d Array
        '''
        self.array = _list
        self._paramR = None #Rows
        self._paramC = None #Columns
        self.shape()

    
    
    def shape(self):
        self._paramR = len(self.array)
        self._paramC = None if isinstance(self.array[0], (int, float)) else len(self.array[0])
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

    
    def __getitem__(self, column, rows = None):
        if rows == None:
            return self.array[column]
        else:
            return self.array[column][rows]

    def Dot(self, object1):
        # return LinAlgLib_C.Dot(self.array, object2.array)
        if self._paramC != object1._paramC:
            return 0

        return sum(i[0] * i[1] for i in zip(self.array, object1.array))

    def median(self):
        med = 0
        if self._paramR % 2 == 0:
            for i in self.array:
                med += i
            return med/self._paramR
        else:
            return list(sorted(self.array))[int(self._paramR/2)]








class Tensor(TensorList):

    def __init__(self, _list: list[list]) -> None:
        self.array = _list
        self.shape()
    

    def T(self):
        result = [[self.array[j][i] for j in range(self._paramR)] for i in range(self._paramC)]
        return Tensor(result)
    

    def Dot(self, object1):
        if self._paramC != object1._paramR:
            print ("Cannot multiply the two matrices. Incorrect dimensions.")
            return 

        C = [[0 for row in range(object1._paramC)] for col in range(self._paramR)]

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
    test = Tensor([[24,21],[214,214,23]])
    
