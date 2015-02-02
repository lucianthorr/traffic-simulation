
class Road:
    """ Simply stores a list of numbers used to
    determine the car's chance of slowing."""
    def __init__(self):
        self.road = []
        for n in range(1000):
            self.road.append(1.0)
        for n in range(1000):
            self.road.append(1.4)
        for n in range(1000):
            self.road.append(1.0)
        for n in range(1000):
            self.road.append(2.0)
        for n in range(1000):
            self.road.append(1.0)
        for n in range(1000):
            self.road.append(1.2)
        for n in range(1000):
            self.road.append(1.0)

    def get_chance_of_slowing(self,location):
        return self.road[location]
