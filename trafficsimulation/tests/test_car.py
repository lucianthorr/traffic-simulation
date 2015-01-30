from trafficsimulation.car import Car

def test_accelerate():
    car = Car()
    car.speed = 30
    car.accelerate()
    assert car.speed == 32.00
    car.accelerate()
    assert car.speed == (100/3)

def test_distance_to_next():
    pass
    # car1 = Car()
    # car2 = Car()
    # car1.set_location(100)
    # car2.set_location(120)
    # car1.set_next_car(car2)
    # assert car1.distance_to_next_car() == 15
