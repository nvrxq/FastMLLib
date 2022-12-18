from FastMLLib.utils import (
    argmax
)

def accuracy(output, y):
        hit = 0
        output = output.argmax()
        y = y.argmax()
        for y in zip(output, y):
            if(y[0]==y[1]):
                hit += 1

        p = (hit*100)/output.shape[0]
        return p

