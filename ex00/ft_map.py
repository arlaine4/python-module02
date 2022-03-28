import types


def ft_map(function_to_apply, iterable):
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
    for elem in it:
        yield function_to_apply(elem)
