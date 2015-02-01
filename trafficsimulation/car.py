from blackbox import Blackbox
import random

class Car:
    def __init__(self,length=5,speed=0,location=0,
                 current_time=0,road=None,number=-1):
        self.number = number
        self.length = length
        self.speed = speed
        self.location = location
        self.next_car = 0
        self.max_speed = (100/3) #meters/second
        self.distance_from_car_ahead = 0
        self.blackbox = Blackbox(-1,self.location,self.speed)
        self.road = road
        self.road_length = len(self.road.road)


    def __str__(self):
        print("Location: {} Speed: {}".format(self.location,self.speed))

    def distance_to_next_car(self):
        """ Distance to next car is the distance from next car's location
        minus this location MINUS the length of the next car. """
        distance = (self.next_car.location - self.location)
        if distance <= 0:
            distance = ((self.road_length - self.location) +
                        self.next_car.location)
        # Check for a pass
        if (self.road_length - self.next_car.location < 100 and
            self.location < 34):
            print(self.location," ",self.next_car.location)
            print(distance, " ", self.road_length)
            distance = distance - self.road_length
        if 500 > (self.location - self.next_car.location) >= -5:
            print(self.location," ",self.next_car.location)
            return self.location - self.next_car.location
        if (distance % self.road_length) > 500:
            print("Self {} Next {}".format(self.location,self.next_car.location))
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

    def too_close(self):
        safe_zone = self.length*5
        if self.speed >= self.distance_to_next_car()+self.next_car.speed-safe_zone:
            return True
        else:
            return False

    def generate_speed(self):
        self.speed = self.accelerate()
        while self.too_close() and self.speed > 1:
            self.speed -= 1

    def move(self):
        self.location = (self.location + self.speed)%self.road_length


    def passed_next(self):
        # Check if self is at end of track and next is across
        if (self.road_length - self.location < 100 and
            self.next_car.location < 34):
            return False
        elif (self.road_length - self.next_car.location < 100 and
              self.location < 34):
              print("pass")
              print("Loc {} Next {}".format(self.location,self.next_car.location))
              return True
        # Check for a standard pass.
        if 100 > self.location - self.next_car.location > -20:
            return True
            print("pass easy")
        else:
            return False

    def resolve(self):
        safe_zone = self.length*5
        while self.passed_next():
            self.location = (self.location - 1) % self.road_length
            self.speed -= 1
