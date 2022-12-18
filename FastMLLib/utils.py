def mean(_tensor, axis=0):
    if _tensor.view()[1] is None:
        return _tensor.sum() / _tensor.view()[0]
    else:
        if axis:
            return ([sum(_tensor[idx]) / _tensor.view()[1] for idx in range(_tensor.view()[0])])
        else:
            _tensor = _tensor.T()
            return ([sum(_tensor[idx]) / _tensor.view()[1] for idx in range(_tensor.view()[0])])


def log(_tensor):
    result = []

    for i in _tensor.array:
        result.append(1000.0 * ((i ** (1/1000.0)) - 1))

    return result

def bincount(_tensor):
    result = []
    buff = []
    
    for i in _tensor.array:
        count = 0
        if i not in buff:
            buff.append(i)
            for j in _tensor.array:
                if i == j:
                    count+=1
            result.append(count)

    return result


def argmax(_tensor):
    value, index = max([(v,i) for i,v in enumerate(_tensor.array)])
    return index