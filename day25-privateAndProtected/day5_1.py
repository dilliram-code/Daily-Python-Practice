# This program is about the protected member
class Protected:
    def __init__(self):
        self._subject = "Machine learning"


class Access(Protected):
    def __init__(self, level):
        self.level = level
        super().__init__()
        # Protected.__init__(self)

    def access_protected(self):
        print("This is the protected subject: ", self._subject)
        print("The level of the subject is ", self.level)


member1 = Access('difficult')
member1.access_protected()
