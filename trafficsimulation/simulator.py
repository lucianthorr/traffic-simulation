import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
import statistics
from .car import Car
from .road import Road

class Simulator:

    def __init__(self,minutes=60):
        self.max_second = int(minutes * 60)
        self.max_tenth = self.max_second * 10
        self.current_second = 0
        self.current_tenth = 0
        self.trial_info = []
        self.road = Road()
        self.meters_of_road = len(self.road.road)
        self.max_cars = (int(self.meters_of_road/1000) * 30)-1



    def car_check(self,cars):
        """ Test method to be sure the sum of all car lengths + the distances
        between cars == the length of the road. If not, there's an error in the
        car generation frequency. """
        size = 0
        for idx, car in enumerate(cars):
            size += car.distance_to_next_car()
        if size > self.meters_of_road + 1:
            print("Size = {}".format(size))
            return True
        else:
            return False


    def generate_cars(self):
        cars = []
        spacing = self.meters_of_road/self.max_cars
        for n in range(self.max_cars):
            cars.append(Car(number=n,location=n*spacing,road=self.road))
        for n in range(self.max_cars):
            try:
                cars[n].next_car = cars[n+1]
            except:
                cars[n].next_car = cars[0]
        return cars

    def start_simulation(self):
        """ Runs the simulation and returns the list of cars in order to plot
        data later. """
        cars = self.generate_cars()
        self.current_second = 0
        self.current_tenth = 0

        while self.current_second < self.max_second:
        #while self.current_tenth < self.max_tenth:
            """ We want to move the cars but we want to move the car
            at the front of the list first so we iterate from top down. """
            for car in cars:
                car.generate_speed()
            for car in cars:
                car.original_move()
            #for index,car in enumerate(cars):
            #    cars[len(cars)-index-1].resolve()

            self.current_second += 1
            self.current_tenth += 1
            for car in cars:
                car.blackbox.update((car.location,car.speed,car.distance_to_next_car()))
            if self.car_check(cars):
                print("Error: cars passing.")
                return
        return cars

    def run_trials(self,number_of_trials):
        """ Runs a number of simulations and returns a list of simulations,
        each containing a list of cars. """
        trial_info = []
        for n in range(number_of_trials):
            trial_info.append(self.start_simulation())
        return trial_info
