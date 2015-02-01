from trafficsimulation.simulator import Simulator
from trafficsimulation.visualizer import Visualizer
import statistics







if __name__ == '__main__':
    simulation = Simulator()
    trials = simulation.run_trials(1)
    visualizer = Visualizer(trials)
    visualizer.get_averages(trials)
    visualizer.plot_traffic(trials[0])
