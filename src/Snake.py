class Snake:
    def __init__(self, name):
        self.name = name 
    # A simple class
    # attribute
    attr1 = "Reptile"
    attr2 = "Snake"
 
    # A sample method 
    def Hiss(self):
        print('Hiss from', self.name)
        return self.name

if __name__ == "__main__":
        print("I'm called from Snake.py")
        mysnake = Snake("Scales")
        name = mysnake.Hiss()
        print(name)
        assert name == "Scales"