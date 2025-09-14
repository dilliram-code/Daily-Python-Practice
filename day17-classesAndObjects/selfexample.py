# The 'self' word basically represents the current object
class SelfId:

    # constructor
    def __init__(self):
        self.name = "Dilli"
        self.gender = "male"

    def self_id(self):
        print(id(self))


object1 = SelfId()
object2 = SelfId()

object1.self_id()
object2.self_id()

# Observation: We can see the two different ids of the the instance. It is because we have used two different objects which represent two different object for different time
