from menu import MENU, resources

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(drink):
    for item in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total

def check_transaction(total, drink):
    if total < MENU[drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - MENU[drink]['cost'], 2)
        print(f"Here is ${change} in change.")
        resources['money'] += MENU[drink]['cost']
        return True
    
def make_coffee(drink):
    for item in MENU[drink]['ingredients']:
        resources[item] -= MENU[drink]['ingredients'][item]
    print(f"Here is your {drink}. Enjoy!")

def coffee_machine():
    machine_on = True
    while machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == 'off':
            machine_on = False
        elif choice == 'report':
            report()
        else:
            if check_resources(choice):
                payment = process_coins()
                if check_transaction(payment, choice):
                    make_coffee(choice)

coffee_machine()