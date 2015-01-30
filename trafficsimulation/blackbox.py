
class Blackbox:

    def __init__(self, time=0,location=0,speed=0):
        """ The blackbox is going to be a list of tuples that record the global
        simulation's time (in seconds), and the car's location and speed. """
        self.time = time
        self.history = [(time,location,speed)]


    def update(self,stat_tuple):
        self.time += 1
        location = stat_tuple[0]
        speed = stat_tuple[1]
        self.history.append((self.time,location,speed))


    def get_history(self):
        print(self.history)
        times = []
        locations = []
        speeds = []
        for time, location, speed in self.history:
            times.append(time)
            locations.append(location)
            speeds.append(speed)
        return times, locations, speeds


    # Probably won't need, but just in case.
    # def normalize_history(self):
    #     original_time = self.history[0][0][0]
    #     for _ in range(original_time):
    #         self.history.insert(0,(0,0,0))
    #     return self.history
