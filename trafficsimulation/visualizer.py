import statistics
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:

    def __init__(self,trials):
        self.trials = []

    def plot_traffic(self, trial):
        """Receives ONE trial and plots the traffic as a scatter plot of cars
        with X-time and Y-location. """
        for index,car in enumerate(trial):
            times, locations, speeds = car.blackbox.get_per_minute_history()
        #times, locations, speeds = trial[0].blackbox.get_full_history()
            plt.scatter(times,locations)
        plt.show()

    def get_averages(self, trials):
        trial_averages = []
        for trial in trials:
            car_averages = []
            for car in trial:
                time,location,speed = car.blackbox.get_full_history()
                car_averages.append(statistics.mean(speed[60:]))
            print(statistics.mean(car_averages))
            print(statistics.stdev(car_averages))
            trial_averages.append(statistics.mean(car_averages))

        #trial0 = trials[0]
        #car0 = trial0[0]
        #print(car0.blackbox.get_full_history())
        return statistics.mean(trial_averages)
