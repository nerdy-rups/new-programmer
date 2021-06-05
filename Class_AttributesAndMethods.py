#demonstrations of the use of class-variables and class-methods in a single class

class Math:
    pi = 3.14
    @classmethod
    def square_root_pi(cls, abc):
        return cls.pi**0.5+abc

print(Math.square_root_pi(4))
Math.pi = 2.15
print(Math().square_root_pi(4)) # direct class name call can be done with the parentheses also

print("*"*200)

class Person:
    number_of_people = 0
    def __init__(self, name):
        #Person.number_of_people +=1
        Person.add_person()
    @classmethod
    def get_person_count(cls):
        return cls.number_of_people
    @classmethod
    def add_person(cls):
        # return (cls.number_of_people+1) <-- this does not work. Output is 0 and 0;because the variable
        # is not actually modified.
        cls.number_of_people += 1 #<-- this works, because the variable is changed
P1 = Person("Rups")
print(P1.get_person_count())
P2 = Person("RG")
print(P2.get_person_count())
