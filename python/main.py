from car import Car


if __name__ == "__main__":
    print("hola mundo")
    car = Car()
    car.license = "AMK456"
    car.driver = "Jhordy Samuel"
    print(vars(car))

    car2 = Car()
    car2.license = "AKM987"
    car2.driver = "Jhovana Toro" 
    print(vars(car))
