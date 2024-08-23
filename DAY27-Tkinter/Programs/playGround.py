def add(*args):
    total_sum = 0
    for n in args:
        total_sum += n
    # print(type(args))
    return total_sum


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


print(add(3, 5))
print(add(4, 7, 6, 10))

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw['make']
        # self.model = kw['model']
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(make='Toyota', model='Innova')
my_car2 = Car(make='BMW')
print(my_car.model)
print(my_car.make)
print(my_car2.model)
print(my_car2.make)
