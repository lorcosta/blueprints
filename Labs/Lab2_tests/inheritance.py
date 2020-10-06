class Vehicle(object):
    def __init__(self, name, top_speed):
        self.name = name
        self.top_speed = top_speed

    def start(self):
        print "%s going at %d km/h" % (self.name, self.top_speed)


class Car(Vehicle):
    def paint(self, color):
        self.color = color  # Car inherits from Vehicle


v = Vehicle('bicycle', 15)
c = Car('Ferrari', 300)
v.start()
c.start()
c.paint('black')
c.color = "black"
# v.paint('blue')
