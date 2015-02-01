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
            if index > 1000:
                break
            times, locations, speeds, distances = car.blackbox.get_per_minute_history()
        times, locations, speeds, distances = trial[0].blackbox.get_full_history()
        #for n in range(len(times)):
        #    print("{}: Loc:{} Speed:{} Dist:{}".format(times[n],locations[n],speeds[n],distances[n]))
        plt.scatter(times,locations)
        plt.show()

    def get_averages(self, trials):
        trial_averages = []
        for trial in trials:
            car_averages = []
            for car in trial:
                time,location,speed, distance = car.blackbox.get_full_history()
                car_averages.append(statistics.mean(speed[120:]))
            #print(statistics.mean(car_averages))
            #print(statistics.stdev(car_averages))
            trial_averages.append(statistics.mean(car_averages))
        print(statistics.mean(trial_averages))
        return statistics.mean(trial_averages)
