import statistics
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:

    def __init__(self,trials):
        self.trials = []

    def get_averages(self, trials):
        trial_averages = []
        for trial in trials:
            car_averages = []
            for car in trial:
                time,location,speed = car.blackbox.get_full_history()
                car_averages.append(statistics.mean(speed))
            trial_averages.append(statistics.mean(car_averages))
        print(statistics.mean(trial_averages))
        return statistics.mean(trial_averages)
