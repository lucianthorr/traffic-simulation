from blackbox import Blackbox
import random

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
        self.blackbox = Blackbox(current_time,self.location,self.speed)

    def __str__(self):
        print("Location: {} Speed: {}".format(self.location,self.speed))

    def set_location(self,location):
        """ Location is the location of the FRONT of the car. """
        self.location = location % self.road_length

    def set_next_car(self,next_car):
        """ Next car is the car ahead of this car. """
        self.next_car = next_car

    def distance_to_next_car(self):
        """ Distance to next car is the distance from next car's location
        minus this location MINUS the length of the next car. """
        if self.next_car == 0:
            return self.road_length
        else:
            distance = (self.next_car.location - self.location - self.next_car.length)
            return (distance % self.road_length)

    def accelerate(self):
        if random.random() < 0.1:
            self.speed -= 2
        elif self.speed < self.max_speed:
            self.speed += 2
        if self.speed >= self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0
        return self.speed

    def move_for_one_second(self):
        self.accelerate()
        # Tentatively move the car and check for conflict
        original_location = self.location
        self.location = (original_location + self.speed) % self.road_length
        if (self.distance_to_next_car() < self.length*4):
            self.location = (original_location + self.next_car.speed) % self.road_length

        self.blackbox.update((self.location,self.speed))
