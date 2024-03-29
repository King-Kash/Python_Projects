from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

def main():
    running = True
    coffee_menu = Menu()
    register = MoneyMachine()
    machine = CoffeeMaker()
    while running == True:

        user_input = input(f"What would you like? {coffee_menu.get_items()}: ")

        if user_input == "report":
            machine.report()
            register.report()


        elif user_input == "off":
            running = False
        else:
            order = coffee_menu.find_drink(user_input)
            # you can use this to check if a variable actually holds on to a object or not
            if order:
                if machine.is_resource_sufficient(order):
                    print(f"Your order costs ${order.cost}")
                    if register.make_payment(order.cost):
                        machine.make_coffee(order)

    sys.exit()


if __name__ == "__main__":
    main()