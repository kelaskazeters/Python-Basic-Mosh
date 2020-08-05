class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi i am {self.name}")


rafli = Person("Rafliano Ziyad")
rafli.talk()

bob = Person("Bob Smith")
bob.talk()