class Animal:
    def __init__(self, *args):  
        ''' 
            Constructor (we are not supposed to create multiple constructors like this)
            Bad way of creating a constructor.
            In actual multiple constructors cannot be created.
            This is just a hack for it.
        '''
        
        if(len(args)==1):
            self.name=args[0]
        
        if(len(args)==2):
            self.name=args[0]
            self.species=args[1]
        
        if(len(args)==3):
            self.name=args[0]
            self.species=args[1]
            self.age=args[2]

    def make_sound(self, sound):
        return "The animal is {} and says {}".format(self.name, sound)

dog=Animal('Dog','mammal',15)

print(dog.age)
print(dog.species)
print(dog.name)
print(dog.make_sound("woof woof"))