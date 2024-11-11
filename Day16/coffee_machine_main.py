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
        elif choice == "latte":
            print("Dispensing latte...")
        elif choice == "cappuccino":
            print("Dispensing cappuccino...")
        elif choice == "off":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose espresso, latte, or cappuccino.")
        
        # Show prompt again after drink is dispensed
        print("Ready for the next customer!\n")

# Run the coffee machine
coffee_machine()
