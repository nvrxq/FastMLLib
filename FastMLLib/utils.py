def mean(_tensor, axis=0):
    '''
    Calculating list of mean values 
    '''
    if _tensor.view()[1] is None:
        return _tensor.sum() / _tensor.view()[0]
    else:
        if axis:
            return ([sum(_tensor[idx]) / _tensor.view()[1] for idx in range(_tensor.view()[0])])
        else:
            _tensor = _tensor.T()
            return ([sum(_tensor[idx]) / _tensor.view()[1] for idx in range(_tensor.view()[0])])


def log(_tensor):
    '''
    Calculating expon. logarithm
    '''
    result = []

    for i in _tensor.array:
        result.append(1000.0 * ((i ** (1/1000.0)) - 1))

    return result




def bincount(_tensor):
    '''
    Count number of occurrences of each value in array of non-negative ints.
    '''
    result = []
    buff = []

    for i in _tensor.array:
        count = 0
        if i not in buff:
            buff.append(i)
            for j in _tensor.array:
                if i == j:
                    count += 1
            result.append(count)

    return result


def argmax(_tensor):
    '''
    Returns the indices of the maximum values along an axis.
    '''
    value, index = max([(v, i) for i, v in enumerate(_tensor.array)])
    return index


def median(_tensor, paramR):
    '''
    Compute the median.
    '''
    med = 0
    if _paramR % 2 == 0:
        for i in _tensor:
            med += i
        return med/_paramR
    else:
        return list(sorted(_tensor))[int(_paramR/2)]


def dot(_tensor, object1):
    '''
    Dot product of two arrays
    '''

    return sum(i[0] * i[1] for i in zip(_tensor, object1))


def square(_tensor):
    return [item**2 for item in _tensor]


def summary(_tensor):
    return sum(_tensor)

def division(_tensor, scalar):
    return [item / scalar for item in _tensor]