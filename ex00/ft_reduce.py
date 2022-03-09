import types


def ft_reduce(function_to_apply, iterable):
    if not isinstance(function_to_apply, types.FunctionType):
        return None
    try:
        it = iter(iterable)
    except TypeError:
        return None
    res = next(it)
    for elem in it:
        res = function_to_apply(res, elem)
    return res
