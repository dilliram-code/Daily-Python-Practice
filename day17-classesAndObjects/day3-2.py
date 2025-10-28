class Army:
    def __init__(self, rank, age, address):
        self.rank = rank
        self.age = age
        self.address = address

    def profile(self):
        print("Rank: ", self.rank, "\nAge: ",
              self.age, "\nAddress: ", self.address)


army1 = Army("Senior", 65, "Kathmandu")
army2 = Army("Subedar", 45, "Dhangadhi")
army3 = Army("Junior", 23, "Kapilvastu")

# # army1 profile
# army1.profile()

# # army2 profile
# army2.profile()

# # army3 profile
# army3.profile()

# LOOPING THE RESULT
army_list = [army1,  army2, army3]
for army in army_list:
    army.profile()
    print("____________________________________")


# Observe the dictionary the each instance separately
for dictionary in army_list:
    print(dictionary.__dict__)
    print("____________________________________")


# Observe the dictionary of the class
print(Army.__dict__)
