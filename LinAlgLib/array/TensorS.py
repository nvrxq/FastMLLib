class TensorList:


    #Protected
    _paramR = None #Rows
    _paramC = None #Columns
    #########################

    def __init__(self, _list: list) -> None:
        '''
        TensorList
        _list = 1d Array
        '''
        self.array = _list
        TensorList.shape(self.array)

    
    @classmethod
    def shape(cls, array):
        cls._paramR = len(array)
        cls._paramC = None if isinstance(array[0], (int, float)) else len(array[0])
        if cls._paramC:
            for idx in range(cls._paramR):
                if len(array[idx]) != cls._paramC:
                    cls._paramC = None
                    break 
        else:
            pass
    
    def __repr__(self) -> str:
        return f"FastLinAlg.TensorList:{self.array}"
        
    
    def __len__(self):
        return len(self.array)

    @classmethod
    def view(cls):
        return (cls._paramR, cls._paramC)



class Tensor(TensorList):

    def __init__(self, _list: list[list]) -> None:
        self.array = _list
        Tensor.shape(self.array)



if __name__ == "__main__":
    test = Tensor([[24,21],[214,214,23]])
    print(test.view())
