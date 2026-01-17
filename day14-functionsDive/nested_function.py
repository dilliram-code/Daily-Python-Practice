# a function inside another function is called a nested function

def outer():
  print("I am from outer function")
  def inner():
    print("I am from inner function")
  print("outer function ends here")

outer()         # outer function is called here

# THINK 🤔 => what will be output here? Will be the inner function executed?
# ???
# No, inner function will not be executed as it is not called anywhere, only defined.
