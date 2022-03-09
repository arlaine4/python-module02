import os
import time
from random import randint


class log:

    def __init__(self, func_ptr):
        self.func = func_ptr

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        call = self.func(machine, *args, **kwargs)
        fd = open('machine.log', 'a+')
        f_name = ' '.join(word.capitalize() for word in self.func.__name__.split('_'))
        user_name = os.environ['USER']
        end = time.time()
        exec_time = end - start_time
        format_time = 'ms' if exec_time < 1. else 's'
        text = f'({user_name})Running: {f_name:20} [ exec-time = {exec_time:.3f} {format_time} ]\n'
        fd.write(text)
        return call


class CoffeeMachine:

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
