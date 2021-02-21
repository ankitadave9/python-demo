class Pizza:

    def __init__(self,base,sauce,topping1,topping2, topping3):
        self.base = base
        self.sauce = sauce
        self.topping1 = topping1
        self.topping2 = topping2
        self.topping3 = topping3

    def makePizza(self):
        return "your pizza base {} with {} and toppings are {},{},{}".format(self.base,self.sauce,self.topping1,self.topping2,self.topping3)

peproni = Pizza('thin crust','pizza sauce','peproni','jelopenos','chesse')
maxican = Pizza('deep pan','bbq','chicken','tomatoes','spicy_chesse')

print(peproni.makePizza())
print(maxican.makePizza())
