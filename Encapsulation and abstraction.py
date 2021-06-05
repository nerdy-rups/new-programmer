# illustration of using private variables and methods in a class

class Price:
    def __init__(self, checkout_price):
        self.__checkout_price = checkout_price
    def __set_discount(self, discount): # arguement of this method in this program is getting passed from
        # the method call. So the code works without having to specify the arguement during object creation.
        return self.__checkout_price*(discount/100)
    def set_final_price(self, discount_given):
        self.__checkout_price = self.__checkout_price - self.__set_discount(discount_given)
    def get_final_price(self):
        print("The final price is", self.__checkout_price)
price = Price(200)
# print(price.checkout_price) <-- # this line won't work because the checkout_price variable is a private variable
price.set_final_price(10)
price.get_final_price()



