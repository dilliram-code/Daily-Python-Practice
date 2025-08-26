# Posional and keyword arguments example
def iamFunction(*args, **kwargs):
  print("Args:", args)
  print("Kwargs:", kwargs)

# iamFunction(1,2,3, fourth = 5, fifth = 6)

# Note down: positional arguments are returned in a tuple whereas keyword arguments are returned in a dictionary.


# Default argument evaluation & mutable defaults pitfall
