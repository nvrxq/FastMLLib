def mean(_tensor, axis=0):
    if _tensor.view()[1] is None:
        return _tensor.sum() / _tensor.view()[0]
    else:
        if axis:
            return ([sum(_tensor[idx]) / _tensor.view()[1] for idx in range(_tensor.view()[0])])
        else:
            _tensor = _tensor.T()
            return ([sum(_tensor[idx]) / _tensor.view()[1] for idx in range(_tensor.view()[0])])
