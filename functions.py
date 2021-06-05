# illustration of shadowing
def function1(number):
    print("the number you entered is", number)

number = 123
function1(90)
print(number)

print("*" * 200)

# illustration of *args
def function2(*arguements):
    for i in arguements:
        print(i)
function2("my", "name", "is", "rupsha")

print("*" * 200)

# illustration of **kwargs
def function3(**key_arguements):
    for j,k in key_arguements.items():
        print(k, j);
        print(j, k)
function3(who = "I", what="am", name="Rupsha")

print("*" * 200)

# illustrating use of None, return for conditional termination and boolean operation

def function4(value = True):
    print ("Three"); print("Two"); print("one")
    if value != True:
        return
    else:
        return "happy birthday"

import random

random_number = random.randint(0,1) # the method could habve been used inside the function invocation directly
is_birthday = function4(random_number)
if is_birthday is None:
    print("Its not your birthday today")
if is_birthday is not None:
    print(is_birthday)

print("*" * 200)

# illustration of None as result of an undefined branch in condition
def strangeFunction(n):
    if(n % 2 == 0):
        return 121212
print(strangeFunction(17))

print("*" * 200)

# using an iterable as function arguement
def function5(iterable):
    sum = 0
    for item in iterable:
        sum +=1
    return sum
sum_of_iterations = function5([5,6,7,3,0])
print (sum_of_iterations)
sum_of_iterations = function5((1,1,1,1))
print (sum_of_iterations)

print("*" * 200)

# using iterable as function result

def function6():
    try:
        function_list = []
        function_input = int(input("Enter the range"))
        for item in range(function_input):
            function_list.append(item)
        return function_list
    except:
        print("Invalid input")
print (function6())

print("*" * 200)

#illustrating use of global keyword:

def function7():
    global var
    var = 2
    print("Do I know that variable?", var)
var = 1
function7()
print(var)

print("*" * 200)

# illustration of looping through a dictionary

def items_in_list(my_dictionary):
    for item in sorted(my_dictionary.keys()):
        print (item, "-->", my_dictionary[item])

my_dict = {"One":"Uno", "Two":"Dos", "Three":"Tres", "Four":"Cuatro", "Five":"Cinco"}
print(items_in_list(my_dict))
