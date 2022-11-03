class Car():
    def __init__(self, marka, model, wheels):
        self.marka = marka
        self.model = model
        self.wheels = wheels
        print(self.model + ' ' + self.marka)


class Animal(Car):
    pass


car = Car(
    model='Camry',
    marka='Toyota',
    wheels=4
)
print(car)


# toyota_camry = Animal()
# lada = Car()
# dog = Animal()
#
# if isinstance(toyota_camry, Car):
#     print('Yes it is')
# else:
#     raise ValueError
#
# print(issubclass(Animal, Car))
# print(issubclass(Car, Animal))

class Number:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return '{}'.format(self.amount)
    # def __str__(self):
    #     return '{}'.format(self.amount)


Num1 = Number(3)
Num2 = Number(10)
print(Num2)
print([Num1, Num2])



list_a = [1, 2, 3]
gen_b = (x for x in list_a)
list_a = [0]
for val in gen_b:
    print(val)
print(list_a)
