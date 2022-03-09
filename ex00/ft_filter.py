import types


def ft_filter(function_to_apply, iterable):
    if not isinstance(function_to_apply, types.FunctionType):
        return None
    try:
        it = iter(iterable)
    except TypeError:
        return None
    for elem in it:
        ret_value = function_to_apply(elem)
        if ret_value is True:
            yield elem
        else:
            continue
