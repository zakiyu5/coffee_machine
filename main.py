from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
money_machine.report()
# another class object for coffee maker
coffee_maker  = CoffeeMaker() 
coffee_maker.report()
# another class object for menu
menu = Menu()

is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}): ").lower()
    if choice ==  "off" :
       is_on = False
    elif choice == "report":
       coffee_maker.report()
       money_machine.report()
    else:
       drink  = menu.find_drink(choice)
       print(drink)
       if coffee_maker.is_resource_sufficient(drink):
          if money_machine.make_payment(drink.cost):
              coffee_maker.make_coffee(drink)