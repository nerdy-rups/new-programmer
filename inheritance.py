from oop import calculator

class child(calculator):
    num2 = 20
    def getCompleteData(self):
        return(self.num, self.num2) #in child class also, the self needs to be used.

ChObj = child()
DataReturned = ChObj.getCompleteData()
print(DataReturned)

class child2(calculator):
    num3 = 30
    def getFullData(self):
        return(self.num3+calculator.summation(self, 10, 20)) # the parent class's instantiations need to be part of the child class code. 
    
ChObj2 = child2()
print(ChObj2.getFullData())



from oop import calculator2

class child3(calculator2):
    def __init__(self):
        # if the parent class has defined init method, that needs to be called and passed values in the child class as well 
        calculator2.__init__(self, 140, 50)
    
ChObj3 = child3()
subtraction_result = ChObj3.subtraction()
print(subtraction_result)
