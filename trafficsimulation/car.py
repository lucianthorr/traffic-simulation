from blackbox import Blackbox
import random

class Car:
    def __init__(self,length=5,speed=0,
                 current_time=0,road=None,number=999):
        self.number = number
        self.length = length
        self.speed = speed
        self.location = 0
        self.next_car = 0
        self.max_speed = (100/3) #meters/second
        self.distance_from_car_ahead = 0
        self.blackbox = Blackbox(current_time,self.location,self.speed)
        self.road = road
        self.road_length = len(self.road.road)

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
        distance = (self.next_car.location - self.location - self.next_car.length)
        if distance < 0:
            distance = ((self.road_length - self.location) +
                        self.next_car.location - self.next_car.length)
        return (distance % self.road_length)

    def accelerate(self):
        road_condition = self.road.get_chance_of_slowing(int(self.location))
        if random.random() < (0.1 * road_condition):
            self.speed -= 2
        elif self.speed < self.max_speed:
            self.speed += 2
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0
        return self.speed

    def move_for_one_second(self):
        self.speed = self.accelerate()
        # Tentatively move the car ahead and check for conflict
        original_location = self.location
        if self.speed < self.distance_to_next_car():
            self.location = (original_location + self.speed) % self.road_length
            if (self.distance_to_next_car() < 100):
                dist_speed = (self.next_car.location - self.location)%self.road_length
                loc_speed = (original_location + self.next_car.speed) % self.road_length
                self.speed = min([dist_speed,loc_speed])
                self.speed = 0
                self.location = (original_location + self.speed) % self.road_length
                #self.location = (original_location + self.next_car.speed) % self.road_length
                #self.speed = self.next_car.speed

        else:
            dist_speed = (self.next_car.location - self.location)%self.road_length
            loc_speed = (original_location + self.next_car.speed) % self.road_length
            self.speed = min([dist_speed,loc_speed])
            self.speed = 0
            self.location = (original_location + self.speed) % self.road_length
            # self.location = (original_location + self.next_car.speed) % self.road_length
            # self.speed = self.next_car.speed

        # Update car's history
        self.blackbox.update((self.location,self.speed))
