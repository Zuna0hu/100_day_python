from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

# all menu items
options = menu.get_items()

def coffee_machine():
    while True:
        # Prompt the user for their choice
        # choice = input("What would you like? (espresso/latte/cappuccino/ or type 'off' to quit): ").lower()
        choice = input(f"What would you like? ({options} or type 'off' to quit): ").lower()

        if choice == "off":
            print("Goodbye!")
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:

            item = menu.find_drink(choice) # return a MenuItem object if it exists

        # # Check the user's input and dispense the drink
        # if choice == "espresso":
        #     print("Dispensing espresso...")
        #     if (coffee_maker.is_resource_sufficient(menu.menu[1])): # if the resources are sufficient
        #         # customer needs to pay
        #         print(f"That should be ${menu.menu[1].cost}.")
        #         if (money_machine.make_payment(menu.menu[1].cost)):
        #             coffee_maker.make_coffee(menu.menu[1])
        # elif choice == "latte":
        #     print("Dispensing latte...")
        #     if (coffee_maker.is_resource_sufficient(menu.menu[0])):
        #         print(f"That should be ${menu.menu[0].cost}.")
        #         if (money_machine.make_payment(menu.menu[0].cost)):
        #             coffee_maker.make_coffee(menu.menu[0])
        # elif choice == "cappuccino":
        #     print("Dispensing cappuccino...")
        #     if (coffee_maker.is_resource_sufficient(menu.menu[2])):
        #         print(f"That should be ${menu.menu[2].cost}.")
        #         if (money_machine.make_payment(menu.menu[2].cost)):
        #             coffee_maker.make_coffee(menu.menu[2])
            if (item != None):
                print(f"Dispensing {item.name}...")
                if (coffee_maker.is_resource_sufficient(item)): # if the resources are sufficient
                    # customer needs to pay
                    print(f"That should be ${item.cost}.")
                    if (money_machine.make_payment(item.cost)):
                        coffee_maker.make_coffee(item)
            else:
                print("Invalid option. Please choose espresso, latte, or cappuccino.")
        
        # Show prompt again after drink is dispensed
        print("Ready for the next customer!\n")


# Run the coffee machine
coffee_machine()
