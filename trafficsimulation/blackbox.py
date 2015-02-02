
class Blackbox:

    def __init__(self, time=-1,location=0,speed=0,distance=0):
        """ The blackbox is going to be a list of tuples that record the global
        simulation's time (in seconds), and the car's location and speed. """
        self.time = time
        self.history = [(self.time,location,speed,distance)]


    def update(self,stat_tuple):
        """ Appends a new tuple of data to the history list. """
        self.time += 1
        location = stat_tuple[0]
        speed = stat_tuple[1]
        distance = stat_tuple[2]
        self.history.append((self.time,location,speed,distance))



    def get_full_history(self):
        """ Returns the car's entire data storage. """
        times = []
        locations = []
        speeds = []
        distances = []
        for time, location, speed, distance in self.history:
            times.append(time)
            locations.append(location)
            speeds.append(speed)
            distances.append(distance)
        return times, locations, speeds, distances

    def get_per_minute_history(self):
        " Returns one second of data for every 60 seconds. """
        times = []
        locations = []
        speeds = []
        distances = []
        for time, location, speed, distance in self.history:
            if time % 60 == 0:
                times.append(time)
                locations.append(location)
                speeds.append(speed)
                distances.append(distance)
        return times, locations, speeds, distances

    def get_current_time(self):
        return self.time
