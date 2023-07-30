class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("inhale the good shit, exhale the bullshit")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    def breathe(self):
        super().breathe()
        print("in water only")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.num_of_legs = 4

    def breathe(self):
        # super().breathe()
        print("on land only")


fish = Fish()
fish.num_of_eyes = 3
mammal = Mammal()
mammal.breathe()
fish.breathe()
print(fish.num_of_eyes)
print(mammal.num_of_eyes)
