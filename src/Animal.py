class Animal:
       
    # Class Variable
    animal = 'animal' 
    greeting = "Nada"    
       
    # The init method or constructor
    def __init__(self,name):
           
        # Instance Variable
        self.name = name       
   
    # Adds an instance variable 
    def speak(self):
        print(self.greeting, 'from', self.name)
        return self.name

    def get_name(self):
        return self.name    

if __name__ == "__main__":
        print("I'm called from Animal.py")
        myanimal = Animal("SomeAnimal")
        name = myanimal.speak()
        print(name)
        #assert name == "Fluffy1"
        assert name == "SomeAnimal"
        print(myanimal.animal)
        print(myanimal.name)
