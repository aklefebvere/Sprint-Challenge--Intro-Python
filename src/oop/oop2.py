# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.


class GroundVehicle():
    # if user does not specify num_wheels, it defaults to 4
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # method that prints out "vroooom"
    def drive(self):
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    # overwrites the init num_wheels from the
    # GroundVehicle class and sets it to 2
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels=2)

    # overwrites the GroundVehicle method drive
    # and sets it to "BRAAAP!!"
    def drive(self):
        return "BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
print(*[vehicle.drive() for vehicle in vehicles], sep='\n')
