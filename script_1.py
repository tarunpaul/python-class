class Animal:
    species = "Multi Cell"

    def __init__(self):
        print("From animal class")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        print("from Dog class")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        print("from Cat class")

dog1 = Dog("Bruno")

cat1 = Cat("Meo")
