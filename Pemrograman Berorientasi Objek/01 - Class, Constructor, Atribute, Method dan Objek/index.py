# This is Class
class Hero:
    # This is Constructor
    def __init__(self, name, power): # Name and Power is Parameters
        # This is Atribute
        self.name = name
        self.power = power

    # This is Method
    def showInfo(self):
        print("Name: {}, Power: {}".format(
            self.name,
            self.power
        ))

# This is Object not Variable
Hero = Hero("Lesly", 500)
Hero.showInfo()