# This is the tiny project to create a range function using generator:

def range_function(start, end):
  for i in range(start, end):
    yield i 

gen = range_function(10,15)

for i in gen:
  print(i)