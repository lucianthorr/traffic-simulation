import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
import statistics
from .car import Car
from .road import Road

class Simulator:

    def __init__(self,meters_of_road=1000,max_cars=30,minutes=60):
        self.meters_of_road = meters_of_road
        self.max_cars = max_cars
        self.max_second = int(minutes * 60)
        self.current_second = 0
        self.trial_info = []


    def check_to_add_cars(self, new_car, cars):
        """ Check for cars ahead and check for cars at the end of the circular
        track. """
        for car in cars:
            if car.location - car.length < 20:
                return False
            elif self.meters_of_road - new_car.length - car.location < 20:
                return False
        else:
            return True

    def possibly_add_car(self,cars):
        if len(cars) < self.max_cars:
            new_car = Car(current_time=self.current_second)
            if (self.check_to_add_cars(new_car, cars)
                and random.random() < 0.1):
                cars.insert(0,new_car)
                """ Each car has a next_car pointer to the car in front of it.
                If we are at max_cars, the first car's next_car points to
                the very newest (and last) car. """
                if 1 < len(cars) < self.max_cars:
                    cars[0].next_car = cars[1]
                elif len(cars) == self.max_cars:
                    cars[self.max_cars-1].next_car = cars[0]
        return cars

    # Probably won't need.  Use in blackbox
    # def normalize_history(self,history):
    #     """Takes a car's history and adds the time before it existed"""
    #     print(len(history))
    #     original_time = history[0][0]
    #     print(original_time)
    #     for _ in range(original_time):
    #         history.insert(0,(0,0))
    #     print(len(history))
    #     return history


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
                cars[len(cars)-index-1].move_for_one_second()
            self.current_second += 1

        average_speeds = []
        for index,car in enumerate(cars):
            times, locations, speeds = car.blackbox.get_per_minute_history()
            #print("Car {} average speed {}".format(len(cars)-index,statistics.mean(speeds)))
            plt.scatter(times,locations)
        plt.show()
        return cars

    def run_trials(self,number_of_trials):
        """ Runs a number of simulations and returns a list of simulations,
        each containing a list of cars. """
        trial_info = []
        for n in range(number_of_trials):
            trial_info.append(self.start_simulation())
        return trial_info
