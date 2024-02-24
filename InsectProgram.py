import InsectClass as ic

def main():
    mosquito = ic.Insect("mosquito")
    house_fly = ic.Insect("house fly")

    mosquito.calc_length_of_flight()
    house_fly.calc_length_of_flight()

    print(f"This is a {mosquito.type}, it has {mosquito.legs} legs, {mosquito.wings} wings and it flies {mosquito.flight_length} miles")
    print(f"This is a {house_fly.type}, it has {house_fly.legs} legs, {house_fly.wings} wings and it flies {house_fly.flight_length} miles")

# create a housefly instance
    
main()