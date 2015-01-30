import matplotlib.pyplot as plt
import random
from .car import Car
from .road import Road

class Simulator:

    def __init__(self,meters_of_road=1000,max_cars=10,minutes=10):
        self.meters_of_road = meters_of_road
        self.max_cars = max_cars
        self.max_second = int(minutes * 60)
        self.current_second = 0


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
        current_num_of_cars = len(cars)
        if len(cars) < self.max_cars:
            new_car = Car(current_time=self.current_second)
            if (self.check_to_add_cars(new_car, cars)
               and random.random() < 0.1):
               cars.append(new_car)
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
        cars = []
        self.current_second = 0
        while self.current_second < self.max_second:
            cars = self.possibly_add_car(cars)

                # If there's space for a car, maybe add a car
                # Add car to list of cars
            for car in cars:
                car.move_for_one_second()
            self.current_second += 1

        for car in cars:
            times, locations, speeds = cars[0].blackbox.get_history()
            plt.scatter(times,locations)
        plt.show()
