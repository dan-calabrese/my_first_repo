from car import Car

car_list = []

with open("cars.txt") as file:
    for line in file:
        info = line.strip().split()
        car = Car(info[0],info[1],int(info[2]),int(info[3]))
        car_list.append(car)

for i in range(2):
    car_list[i].drive()
    print(car_list[i].get_gas_tank())
    print(car_list[i].get_odometer())
    print(car_list[i])

# for car in car_list:
#         print(car.get_gas_tank())
#         print(car.get_odometer())
