# This project is aimed to make the for loop using iter() and next() function. The main purpose of this project is to understand the working of the for loop.


def my_for_loop(iterable):
  # make the iterable an iterator using iter()
  my_iterator = iter(iterable)
  
  while True:
    try:
      print(next(my_iterator)) 
    except StopIteration:
      break


my_list = ['a', 'b', 'c', 'd', 'e']
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
my_set = {1, 2, 3, 4, 5}
my_tuple = ("Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday")

my_for_loop(my_tuple)    # pass any iterables: list, dict, set, tuple

