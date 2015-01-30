from trafficsimulation.simulator import Simulator
from trafficsimulation.visualizer import Visualizer
import statistics

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





if __name__ == '__main__':
    simulation = Simulator()
    trials = simulation.run_trials(1)
    visualizer = Visualizer(trials)
    visualizer.get_averages(trials)
