class Nepal:
    def __init__(self, continent, climate):
        # Instance Variable
        self.continent = continent
        self.climate = climate

    def show_info(self):
        print("Continent's Name ", self.continent)
        print("Climate in Nepal ", self.climate)


nepal1 = Nepal("Asia", "Mixed")

# dictionary of the nepal1 object
print("The content of the object's dictionary are: ")
print(nepal1.__dict__)

# looping the key pair for each element
for key, value in nepal1.__dict__.items():
    print(key, "=", value)
