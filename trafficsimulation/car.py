from blackbox import Blackbox

class Car:
    def __init__(self,length=5,speed=0,acceleration=2,
                 road_length=1000,current_time=0):
        self.length = length
        self.speed = speed
        self.acceleration = acceleration
        self.location = 0
        self.next_car = 0
        self.max_speed = (100/3) #meters/second
        self.distance_from_car_ahead = 0
        self.road_length = road_length
        self.blackbox = Blackbox(current_time)

    def set_location(self,location):
        """ Location is the location of the FRONT of the car. """
        self.location = location % self.road_length

    def set_next_car(self,next_car):
        """ Next car is the car ahead of this car. """
        self.next_car = next_car

    def distance_to_next_car(self):
        """ Distance to next car is the distance from next car's location
        minus this location MINUS the length of the next car. """
        distance = (self.next_car.location - self.location - self.next_car.length)
        return distance

    def accelerate(self):
        if self.speed < self.max_speed:
            self.speed += 2
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        return self.speed

    def move_for_one_second(self):
        self.accelerate()
        #if (self.distance_to_next_car() + self.speed) > 20:
        self.location = (self.location + self.speed) % self.road_length
        #self.time += 1
        self.blackbox.update((self.location,self.speed))

        #else:
