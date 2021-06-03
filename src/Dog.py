class Dog:
    def __init__(self, name):
        self.name = name 
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method 
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

Fido = Dog("Cuddles")
print(Fido.name)