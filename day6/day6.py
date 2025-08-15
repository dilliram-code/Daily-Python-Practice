from random import randrange as rg
from random import randrange
import random
from random import randint

num = randint(1, 11)
print(num)


num1 = random.randrange(1, 90)
print(num1)


num2 = randrange(8, 88)
print(num2)


num3 = rg(6, 66)
print(num3)

# NOTE: We can specify the step for the randrange function
result = random.randrange(0, 100, 5)
print(result)

''' NOTE: The first and the last number are exclusive
first_number: It represents the starting
middle one: represents the end of the range
last one: represents the step that would be used

# NOTE: Both randint() and randrange() cannot produce
float value number
'''

# Random number of specific length

random_number = random.randint(1000, 9999)
print(random_number)

# Both the lower and upper limit are included here
# import random
rand_num = random.randint(10, 10000)
print(rand_num)


# This will generate the four digits always
randrange_number = random.randrange(1000, 2000)
print(randrange_number)


# Using the random module for for loop

for i in range(5):
    print(random.randint(-10, 10), end=' ')


# random.choice()
# We can use random.choice() to choose any number from
# a given list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

chosen_number = random.choice(my_list)
print(chosen_number)


# We can use the random module with not number but also
# with the strings

fruits = ['banana', 'apple', 'mango', 'pineapple', 'pear']

# import the random module

# make a selection
my_selection = random.choice(fruits)

# print the result
print(my_selection)


# In this range function, last index will not be
# included

number_list = []
for i in range(1, 11):
    number_list.append(random.randint(1, 100))

print(number_list)


# We can also construct a function which returns the
# list of the random numbers

def random_generator():
    import random
    fill_me = []

    for i in range(0, 11):
        fill_me.append(random.randint(10, 101))
    return fill_me


result = random_generator()
print(result)


# Unique random numbers
# We can generate the unique random numbers using
# sample() function


# # ten unique numbers from 1 to 100
my_list = random.sample(range(1, 100), 10)
print(my_list)


# Python's NumPy module has a numpy.random package to generate
# random data


# Use of seed for the same value every time

random.seed(7)

my_number = random.randint(1, 11)
print(my_number)


# In the result for the code above, we can see that
# result generated will always be same every time
