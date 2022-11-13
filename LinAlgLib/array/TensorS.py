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

    def Dot(self, object2):
        return LinAlgLib_C.Dot(self.array, object2.array)






class Tensor(TensorList):

    def __init__(self, _list: list[list]) -> None:
        self.array = _list
        self.shape()
    

    def T(self):
        result = [[self.array[j][i] for j in range(self._paramR)] for i in range(self._paramC)]
        return Tensor(result)
    
    #def d(self):
     #   return LinAlgLib_C.d(self.array)





if __name__ == "__main__":
    test = Tensor([[24,21],[214,214,23]])
    
