import menu

water_amount = menu.resources["water"]
milk_amount = menu.resources["milk"]
coffee_amount = menu.resources["coffee"]
coffers = 0

def make_coffee(order, money):
    global water_amount
    global milk_amount
    global coffee_amount
    global coffers
# resources need to be checked first and then money is checked last

    if order == "espresso":
        if water_amount >= menu.MENU["espresso"]["ingredients"]["water"]:
            if coffee_amount >= menu.MENU["espresso"]["ingredients"]["coffee"]:
                if money >= menu.MENU["espresso"]["cost"]:
                    water_amount -= menu.MENU["espresso"]["ingredients"]["water"]
                    coffee_amount -= menu.MENU["espresso"]["ingredients"]["coffee"]
                    coffers += menu.MENU["espresso"]["cost"]
                    change = round(money - menu.MENU["espresso"]["cost"], 2)
                    print(f"Your change is ${change}")
                    print("Enjoy your espresso ☕️!")
                else:
                    print("Sorry you do not have enough money. Refund issued.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    elif order == "latte":
        if water_amount >= menu.MENU["latte"]["ingredients"]["water"]:
            if coffee_amount >= menu.MENU["latte"]["ingredients"]["coffee"]:
                if milk_amount >= menu.MENU["latte"]["ingredients"]["milk"]:
                    if money >= menu.MENU["latte"]["cost"]:
                        water_amount -= menu.MENU["latte"]["ingredients"]["water"]
                        coffee_amount -= menu.MENU["latte"]["ingredients"]["coffee"]
                        coffers = coffers + menu.MENU["latte"]["cost"]
                        change = round(money - menu.MENU["latte"]["cost"], 2)
                        print(f"Your change is ${change}")
                        print("Enjoy your latte ☕️!")
                    else:
                        print("Sorry you do not have enough money. Refund issued.")
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")

        else:
            print("Sorry there is not enough water.")
    elif order == "cappuccino":
        if water_amount >= menu.MENU["cappuccino"]["ingredients"]["water"]:
            if coffee_amount >= menu.MENU["cappuccino"]["ingredients"]["coffee"]:
                if milk_amount >= menu.MENU["cappuccino"]["ingredients"]["milk"]:
                    if money >= menu.MENU["cappuccino"]["cost"]:
                        water_amount -= menu.MENU["cappuccino"]["ingredients"]["water"]
                        coffee_amount -= menu.MENU["cappuccino"]["ingredients"]["coffee"]
                        coffers += menu.MENU["cappuccino"]["cost"]
                        change = round(money - menu.MENU["cappuccino"]["cost"], 2)
                        print(f"Your change is ${change}")
                        print("Enjoy your cappuccino ☕️!")
                    else:
                        print("Sorry you do not have enough money. Refund issued.")
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")

        else:
            print("Sorry there is not enough water.")
    elif order == "report":
        print(f"water:  {water_amount}")
        print(f"milk: {milk_amount}")
        print(f"coffee: {coffee_amount}")
        print(f"money: {coffers}")