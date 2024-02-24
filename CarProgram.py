from CarClass import Car

def main():
    car = Car(2024, "Chevy")

    for i in range(0, 10):
        if i < 5:
            car.accelerate()
            print(car.get_speed())
        elif i >= 5 and i < 10:
            car.brake()
            print(car.get_speed())
        else:
            break
        
        i += 1

main()