from ft_map import *
from ft_filter import *
from ft_reduce import *


def adder(value):
    return value + 10


gen_map = ft_map(adder, [1, 2, 3])
while 1:
    print(next(gen_map))