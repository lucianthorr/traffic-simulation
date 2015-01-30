from trafficsimulation.simulator import Simulator
from trafficsimulation.car import Car

def test_check_to_add_car():
    sim = Simulator()
    car1 = Car()
    car2 = Car()
    car3 = Car()
    new_car = Car()
    new_car.set_location(0)
    car1.set_location(25)
    car2.set_location(50)
    car3.set_location(400)
    assert sim.check_to_add_cars(new_car,[car1,car2,car3]) == True
    car1.set_location(20)
    assert sim.check_to_add_cars(new_car,[car1,car2,car3]) == False
    car1.set_location(30)
    car3.set_location(980)
    assert sim.check_to_add_cars(new_car,[car1,car2,car3]) == False
    car3.set_location(975)
    assert sim.check_to_add_cars(new_car,[car1,car2,car3]) == True
