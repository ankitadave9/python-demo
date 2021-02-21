class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("kenwood", 8.99)
hamilton = Kettle("hemilton", 12.75)

print(kenwood.price)
print("models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 40)

kenwood.power = 1.5
print(kenwood.power)
print("switch to atomic power")  # how to change values
Kettle.power_source = "atomic"

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
