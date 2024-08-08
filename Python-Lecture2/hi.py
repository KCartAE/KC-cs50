# print("hello world!")
# name = input("name :")
# print("hello,", name)

def square(x, y, z):
    return x*y-z
print(square(2,4,5))

class Points():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Points(2,8)
print(p.x)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_pass(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
flight = Flight(3)
people = ["harry", "ron", "hermione", "ginny"]

for person in people:
    success = flight.add_pass(person)
    if success:
        print(f"Add {person} successfully.")
    else:
        print(f"No avaliable seat for {person}.")

        ##############################

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper
@announce
def hello():
    print("hello, world!")

hello()