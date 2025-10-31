# This program is all about understanding the concept of getter and setter
class Animal:
    def __init__(self, color, place, number):
        self.color = color
        self.__number = number
        self.__place = place
    
    def show_details(self):
        print("The color of the animal is ",self.color, "and it is found in ",self.__place,self.__number)
    
    def getter_method(self):
        return self.__place
     
     # setter method
    def setter_method(self,number):
        if number > 50:
            print("The entered number is invalid")
        else:
            self.__number = number
animal1 = Animal("grey",'terai', 10)

#This is before setting the value of number(a private attribute)

#before modify
animal1.show_details()

#invalid number modify
animal1.setter_method(60)

# valid number modify
animal1.setter_method(15)

#show details 
animal1.show_details()