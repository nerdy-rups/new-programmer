class calculator():
    num = 5
   # def __init__(self, a, b): -->>> if these are declared here, all the objects of this class need to declare these instance variables during creation 
     #   self.firstNumber = a 
     #  self.secondNumber = b
    
    def summation(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        return(self.firstNumber+self.secondNumber+self.num)

    def myself(self):
        return self
obj1 = calculator()
sumValue = obj1.summation(3,6)
print(sumValue)
# see this to understand what is self
print(obj1.myself(), end = '')
obj2 = calculator()
print(obj2.myself())


class calculator2():
    def __init__(Shelf, a, b): #The name "self" is a convention. Not an absolution
        Shelf.firstNumber = a
        Shelf.secondNumber = b
        print("I am here! No need to call me")
    
    def subtraction(Shelf): #by default self is taken as an arguement. So, if that is missed during method definition, typeError will be seen
        # initialisation during method definition can be used to override the values instantiated during class defintiton
        #self.firstNumber = a 
        #self.secondNumber = b
        return(Shelf.firstNumber-Shelf.secondNumber)

obj3 = calculator2(90,10)
diffValue = obj3.subtraction()
print(diffValue)

    
#Whenever object is created, self gets called on all the instance variables that are defined in it as well as on any class variables. 


# class can be used without creating objects of it also. 
class myclass():
    def __init__(self, a):
        self.number = a
        print(self.number)

myclass(10)
