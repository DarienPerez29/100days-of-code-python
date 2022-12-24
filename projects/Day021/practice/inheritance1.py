class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Breathing")


class Fish(Animal):
    def __init__(self):
        super.__init__

    def breathe(self):
        super().breathe()
        print("But under water")


nemo = Fish()
nemo.breathe()
any_animal = Animal()
any_animal.breathe()
