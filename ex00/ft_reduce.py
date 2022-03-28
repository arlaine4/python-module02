import types


def ft_reduce(function_to_apply, iterable):
    if not isinstance(function_to_apply, types.FunctionType):
        return None
    try:
        it = iter(iterable)
    except TypeError:
        return None
    try:
        if not callable(function_to_apply):
            raise TypeError('Error1')
        if not hasattr(iterable, '__iter__'):
            raise TypeError('Error2')
        if callable(iterable):
            raise TypeError('Error3')
    except:
        print('TypeError : Object not iterable')
        return None
    res = next(it)
    for elem in it:
        res = function_to_apply(res, elem)
    return res
