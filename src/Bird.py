class Bird:
    def __init__(self, name):
        self.name = name 
    # A simple class
    # attribute
    attr1 = "Bird"
    attr2 = "Bird"
 
    # A sample method 
    def Tweet(self):
        print('Tweet from', self.name)
        return self.name

if __name__ == "__main__":
        print("I'm called from Bird.py")
        mybird = Bird("Tweety")
        name = mybird.Tweet()
        print(name)
        #assert name == "Fluffy1"
        assert name == "Tweety"