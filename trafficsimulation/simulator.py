import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
import statistics
from .car import Car
from .road import Road

class Simulator:

    def __init__(self,minutes=180):
        self.max_second = int(minutes * 60)
        self.current_second = 0
        self.trial_info = []
        self.road = Road()
        self.meters_of_road = len(self.road.road)
        self.max_cars = int(self.meters_of_road/1000) * 30


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


    def possibly_add_car(self,cars):
        timing = int(self.meters_of_road / self.max_cars)
        if len(cars) < self.max_cars and (self.current_second % timing) == 0:
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
        return cars


    def start_simulation(self):
        """ Runs the simulation and returns the list of cars in order to plot
        data later. """
        cars = []
        self.current_second = 0
        while self.current_second < self.max_second:
            cars = self.possibly_add_car(cars)
            """ We want to move the cars but we want to move the car
            at the front of the list first so we iterate from top down. """
            for index,car in enumerate(cars):
                #cars[index].move_for_one_second()
                cars[len(cars)-index-1].move_for_one_second()
            self.current_second += 1
        # times = []
        # locations = []
        # speeds = []
        # times, locations, speeds = cars[29].blackbox.get_full_history()
        # for n in range(3600):
        #     print("{}: {}: {}".format(times[n],locations[n],speeds[n]))
        return cars

    def run_trials(self,number_of_trials):
        """ Runs a number of simulations and returns a list of simulations,
        each containing a list of cars. """
        trial_info = []
        for n in range(number_of_trials):
            trial_info.append(self.start_simulation())
        return trial_info
