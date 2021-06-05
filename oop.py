class Dog:
    def __init__(self, name):
        self.pame = name+" good doggy"
        self.var2 = "this dog barks"
    ''' the first parameter in any method should be self(or whatever that is called) because we invisibly
    need to pass the actual class object so that we know which object we are accessing when we're going to get
    any attribute of the class.'''
    # def set_name(self, Name):
    #     self.name = Name
    def get_name(self):
        return self.pame
    def set_age(self, Age):
        self.age = Age
        print("age is", Age)
    def get_age(self):
        return self.age
d1 = Dog("Tom")
print(d1.pame)
print(d1.var2)
d2 = Dog("Jerry")
print(d2.get_name())
d1.set_age(45)
print(d1.get_age())
# d1 = Dog()
# d1.set_name("Tom"); d1.set_age(46)
# print(d1.get_name()); print(d1.get_age())