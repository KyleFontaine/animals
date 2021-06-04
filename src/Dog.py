class Dog:
    def __init__(self, name):
        self.name = name 
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method 
    def Bark(self):
        print('Woof from', self.name)
        return self.name

if __name__ == "__main__":
        print("I'm called from Dog.py")
        mydog = Dog("Fluffy")
        name = mydog.Bark()
        print(name)
        #assert name == "Fluffy1"
        assert name == "Fluffy"