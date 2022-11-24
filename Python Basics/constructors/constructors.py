class Animal:
    def __init__(self, name, species):  ## Constructor
        self.name=name
        self.species=species

    def __init__(self, name, species, age): ## Constructor being overriden
        self.name=name
        self.species=species
        self.age=age

    def make_sound(self, sound):
        return "The animal is {} and says {}".format(self.name, sound)

dog=Animal('Dog','mammal',15)

print(dog.age)