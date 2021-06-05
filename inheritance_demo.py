'''illustration of simple inheritance using a common class Pet and individual classes cat and dog inheriting it
and also adding their own attributes'''

class Pet:
    def __init__(self, pet_name, pet_age):
        self.name = pet_name
        self.age = pet_age
    def show(self):
        print("Hi. My name is", self.name, "and my age is", self.age)
    def speak(self):
        print("I have nothing to say")

class Cat(Pet):
    def __init__(self, pet_name, pet_age, pet_colour): # here new initialization is needed because new
        # paramenters specific to this class need to be passed.
        super().__init__(pet_name, pet_age) #if this line is removed the code will be erronous because then
        # this Cat class does not have any attribute to identify the 2 parameters common to itself and the
        # parent class
        self.colour = pet_colour
    def speak(self):
        print("I meow")

class Dog(Pet):
    def __init__(self, pet_name, pet_age, pet_colour): # deleting the common parameters and the next line
        # will also lead to errors because then during object creation I cannot pass those 2 common
        # parameters.
        super().__init__(pet_name, pet_age)
        self.colour = pet_colour
    def speak(self):
        print("I bark")

class Fish(Pet):
    #here nothing more is needed because I am allowing it to be a carbon-copy of the parent.
    pass

Doggy = Dog("Tommy", 12, "brown")
Doggy.show()
Doggy.speak()
print("I am also {Doggy.colour}")

Fishy = Fish("Nemo", 15)
Fishy.show()
Fishy.speak()

Catty  = Cat("Billy", 12, "brown")
Catty.show()
Catty.speak()
print("I am also", Catty.colour)
