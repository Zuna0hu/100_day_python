from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

def coffee_machine():
    while True:
        # Prompt the user for their choice
        choice = input("What would you like? (espresso/latte/cappuccino/ or type 'off' to quit): ").lower()

        # Check the user's input and dispense the drink
        if choice == "espresso":
            print("Dispensing espresso...")
            if (coffee_maker.is_resource_sufficient(menu.menu[1])): # if the resources are sufficient
                # customer need to pay
                print(f"That should be ${menu.menu[1].cost}.")
                if (money_machine.make_payment(menu.menu[1].cost)):
                    coffee_maker.make_coffee(menu.menu[1])
        elif choice == "latte":
            print("Dispensing latte...")
            if (coffee_maker.is_resource_sufficient(menu.menu[0])):
                coffee_maker.make_coffee(menu.menu[0])
        elif choice == "cappuccino":
            print("Dispensing cappuccino...")
            if (coffee_maker.is_resource_sufficient(menu.menu[2])):
                coffee_maker.make_coffee(menu.menu[2])
        elif choice == "off":
            print("Goodbye!")
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            print("Invalid option. Please choose espresso, latte, or cappuccino.")
        
        # Show prompt again after drink is dispensed
        print("Ready for the next customer!\n")


# Run the coffee machine
coffee_machine()
