import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
import statistics
from .car import Car
from .road import Road

class Simulator:

    def __init__(self,minutes=120):
        self.max_second = int(minutes * 60)
        self.current_second = 0
        self.trial_info = []
        self.road = Road()
        self.meters_of_road = len(self.road.road)
        self.max_cars = (int(self.meters_of_road/1000) * 30)


    def update_next_cars(self,cars):
        for index,current_car in enumerate(cars):
            min_distance = self.meters_of_road
            for idx, next_car in enumerate(cars):
                distance = (next_car.location - current_car.location - next_car.length)
                if 0 < distance < min_distance:
                    min_distance = distance % self.meters_of_road
                    current_car.next_car = next_car
            if min_distance == self.meters_of_road:
                current_car.next_car = cars[0]


    def add_car(self,cars):
        if len(cars) < self.max_cars:
            new_car = Car(current_time=self.current_second,
                          road=self.road,number=len(cars))
            cars.insert(0,new_car)
            """ Each car has a next_car pointer to the car in front of it.
            If we are at max_cars, the first car's next_car points to
            the very newest (and last) car. """
            if 1 < len(cars) <= self.max_cars:
                cars[0].next_car = cars[1]
                cars[len(cars)-1].next_car = cars[0]
            elif len(cars) == 1:
                cars[0].next_car = cars[0]
            if len(cars) == self.max_cars:
                for car in cars:
                    car.test_time = True
        return cars

    def car_check(self,cars):
        """ Test method to be sure the sum of all car lengths + the distances
        between cars == the length of the road. If not, there's an error in the
        car generation frequency. """
        size = len(cars) * 5
        for idx, car in enumerate(cars):
            #print(car.distance_to_next_car())
            if car.distance_to_next_car() > self.meters_of_road - car.length:
                for car in cars:
                    #print("Car {}: Location: {} Distance: {}".format(car.number,car.location,car.distance_to_next_car()))
                    size += car.distance_to_next_car()
        return size

    def start_simulation(self):
        """ Runs the simulation and returns the list of cars in order to plot
        data later. """
        cars = []
        self.current_second = 0
        while self.current_second < self.max_second:
            cars = self.add_car(cars)
            """ We want to move the cars but we want to move the car
            at the front of the list first so we iterate from top down. """
            for index,car in enumerate(cars):
                #cars[index].move_for_one_second()
                cars[len(cars)-index-1].move_for_one_second()
            self.current_second += 1

            if self.car_check(cars) > (self.meters_of_road + 1):
                #for car in cars:
                #    print("#{} Location: {} Speed:{} Distance to Next: {}".format(car.number,car.location,car.speed,car.distance_to_next_car()))
                #    if(car.distance_to_next_car() > 6000):
                #        print("Loc of next: {}".format(car.next_car.location))
                print("new distance to old = {}".format(cars[0].distance_to_next_car()))
                print("old distance to new = {}".format(cars[len(cars)-1].distance_to_next_car()))
        #time,location,speed,distance = cars[209].blackbox.get_full_history()
        #for n in range(len(time)):
        #    print("T: {}\tLoc: {}\tSpeed: {}\tDis: {}".format(time[n],location[n],speed[n],distance[n]))
                #return
        #print(len(cars))
        return cars

    def run_trials(self,number_of_trials):
        """ Runs a number of simulations and returns a list of simulations,
        each containing a list of cars. """
        trial_info = []
        for n in range(number_of_trials):
            trial_info.append(self.start_simulation())
        return trial_info
