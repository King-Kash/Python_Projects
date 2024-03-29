import menu
import random
import math
import sys
from dispenser import make_coffee

def coin_collector():
    print("please insert coins")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total_value = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total_value

def main():
    running = True
    while running:
        user_order = input("What would you like? (espresso/latte/cappuccino): ")
        if user_order == "espresso" or user_order == "latte" or user_order == "cappuccino":
            money = coin_collector()
            print(money)
            make_coffee(user_order, money)
        elif user_order == "report":
            make_coffee(user_order, 0)
        elif user_order == "off":
            running = False
    sys.exit()


if __name__ == "__main__":
    main()
