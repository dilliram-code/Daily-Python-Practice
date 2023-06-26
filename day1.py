# This is an example os simple inheritance.
class Police:
    def __init__(self, name, station, level):
        self.name = name
        self.station = station
        self.level = level

    def chase(self):
        print("Police chases to the theif.")


class Theif(Police):
    def __init__(self, name, height, color):
        self.name = name
        self.height = height
        self.color = color

    def run(self):
        print("The theif runs when a policeman chases.")


police1 = Police("Ramesh", "Baniyatar", "Sipahi")
police1.chase()

police2 = Theif("Mahes", 5.5, "Blode")
police2.chase()
police2.run()
