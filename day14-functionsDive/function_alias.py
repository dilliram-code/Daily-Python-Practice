def wish(name):
  print("Good morning ", name)

greet = wish

# here reference of the wish function is shared to greet function so both of them are pointing to the same function object

greet("Sanjay")
wish("Dilli")

# print the ids
print(id(greet))
print(id(wish))

# both will point to the same ids, indicating that pointing to the same func obj.