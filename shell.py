import core
import disk
def intro():
    print('\n\tWelcome to Valente\'s 2017 Exotic Cars!')
    msg = input('''\n\tWhich car would you like to see?\n 
    \tType the number of the choice of your car\n
    \t1. Alfa Romeo 4c Coupe
    \t2. Audi R8 V10 Plus
    \t3. BMW i8
    \t4. Corvette z06
    \t5. Cheverlets Camaro
    \t6. Dodge Challenger
    \t7. Dodge Viper
    \t8. Ford Mustang Shelby GT350R
    \t9. Lamborghini Huracan
    \t10. Porche 911 GT3 RS \n''')
    if msg.isnumeric():
        return msg
    else:
        return 'Sorry in has to be in numeric form'
def chosen_car(car, deposit, car_1):
    print('You have chosen',car,'the renting price per day is, $' + str(car_1)+'.')
    print('\nThe deposit of this vihicle will be, $'+str(deposit)+'.')
    return input('''\nWould you like to keep going or would you like to rent this car.\n
    Type in the number of your choice.\n
    \t1. If you would like to rent this car.
    \t2. If you would like to change car.\n''') 

def main():
    cars = disk.list_of_cars()
    choice = intro()
    car = core.choice_of_car(choice, cars)
    deposit = core.replacement(car)   
    car_1 = core.calculate_price_of_renting_with_taxes(car)
    decision = chosen_car(car, deposit, car_1)
if __name__ == '__main__':
    main()