user_input = int(input("Enter the number for which you want factorial"))
factorial = 1
def count_factorial(user_entered_number):
    if user_entered_number == 1:
        return 1
    elif user_entered_number == 2:
        return 2
    elif user_entered_number in range(-999999, 1):
        return "Only positive integers allowed!"
    else:
        for i in range(2, user_entered_number+1):
            global factorial
            factorial *=i
        return factorial
#print(factorial)
print("Your answer is:", count_factorial(user_input))
