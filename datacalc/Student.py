from Pizza import Pizza


class Student:

    def __init__(self, first, last, email, address):
        self.first = first
        self.last = last
        self.email = email
        self.address = address

    def getName(self):
        return self.first+" " +self.last

    def getMail(self):
        return self.email + self.address

indian =  Pizza('thin crust','pizza sauce','peproni','jelopenos','chesse')


ankita = Student("ankita", "dave", "ankitadave@gmail.com", "bs14 8ez")
milan = Student("milan","desai","milandesai@gmail.com","69,bs14")

print(ankita.getName())
print(ankita.getMail())

print(indian.makePizza())
