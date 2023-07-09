# In this tutorial, we will discussing about the class methods and its properties
class City:
    city_name = 'Kathmandu'
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
    def display(self):
        return "City: " + self.name

    def city_detail(cls):
        return "Butwal"

city1 = City("Birgunj", "Medium")
print(City.city_detail())