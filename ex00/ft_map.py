import types


def ft_map(function_to_apply, iterable):
    if not isinstance(function_to_apply, types.FunctionType):
        return None
    try:
        it = iter(iterable)
    except TypeError:
        return None
    for elem in it:
        yield function_to_apply(elem)
