class CallableClass:
    def __init__(self):
        self.counter = 0
    def __call__(self):
        self.counter += 1
        print("I have been called for ", self.counter, " times")

# Create an instance of Callable class
obj = CallableClass()

# Call the instance as if it were a function
obj()
obj()


"""
In this example, the CallableClass defines a __call__() method that increments a counter and prints a message each time the instance is called. By making the class callable, we can create an object obj from the class and then call it as if it were a function. Each time obj() is invoked, the counter is incremented, and a message is printed.

"""