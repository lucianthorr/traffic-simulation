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

    def check_for_pass(self):
        # If self is ahead of next (>0)
        # but not so far that its really behind (<500)
        if 0 < (self.location - self.next_car.location) < 500:
             return True, self.next_car.location - self.location
        elif (self.road_length - self.next_car.location < 100 and
            self.location < 34):

            return True, -1 * ((self.road_length - self.next_car.location)
                          + self.location)
        else:
            return False, None

    def distance_to_next_car(self):
        """ Distance to next car is the distance from next car's location
        minus this location MINUS the length of the next car. """
        distance = (self.next_car.location - self.location)
        if distance < 0:
            distance = ((self.road_length - self.location) +
                        self.next_car.location)
        distance %= self.road_length
        passed, pass_distance = self.check_for_pass()
        if passed:
            return pass_distance
        else:
            return distance

    def accelerate(self):
        road_condition = self.road.get_chance_of_slowing(int(self.location))
        if random.random() < (0.1 * road_condition):
            self.speed -= .2
        elif self.speed < self.max_speed:
            self.speed += .2
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


    def moved_too_far(self):
        safe_zone = self.length*5
        if self.distance_to_next_car() <= safe_zone :
            return True
        else:
            return False

    def resolve(self):
        while self.moved_too_far() and self.speed>0:
            self.location = (self.location - 1) % self.road_length
            self.speed -= 1

    def original_move(self):
        self.speed = self.accelerate()
        dist_speed = self.distance_to_next_car()-5
        min_speed = min([x for x in [dist_speed, self.next_car.speed] if x >= 0])
        # Tentatively move the car ahead and check for conflict
        original_location = self.location
        if (self.speed) <= self.distance_to_next_car()-5:
            self.location = (original_location + self.speed) % self.road_length
            if self.distance_to_next_car() < self.length*5:
                self.location = (original_location + min_speed) % self.road_length
                self.speed = min_speed
        else:
             self.location = (original_location + min_speed) % self.road_length
             self.speed = min_speed
