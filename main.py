from src.Dog import Dog


if __name__ == "__main__":
        print("I'm called from main.py")
        mydog = Dog("Cuddles")
        name = mydog.Bark()
        print(name)
        #assert name == "Fluffy1"
        assert name == "Cuddles"