import sys
from autos import load_factory
from autos import AutoFactory

def ExecuteClassicFactory():
    cars = list()
    for factory_name in 'chevyfactory', 'jeepfactory', 'fordfactory', 'teslafactory':
        factory = load_factory(factory_name)
        cars.append(factory.create_auto())
    return cars

def ExecuteSimpleFactory():
    cars = list()
    factory = AutoFactory()
    for carname in 'ChevyVolt', 'FordFusion', 'JeepSahara', 'Test Roaster':
        cars.append(factory.create_instance(carname))
    return cars

def main():
    args = sys.argv[1:]
    cars = list()
    if len(args) == 0 or args[0] == 'cf':
        print("Classic Factory Pattern\n")
        cars = ExecuteClassicFactory()
    elif args[0] == 'sf':
        print("Simple Factory Pattern\n")
        cars = ExecuteSimpleFactory()
    else:
        print("Invalid arguments!")
    for car in cars:
        car.start()
        car.stop()

if __name__ == '__main__':
    main()
    