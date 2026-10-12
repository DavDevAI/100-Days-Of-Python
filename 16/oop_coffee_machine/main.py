from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from rich.console import Console

mm = MoneyMachine()
men = Menu()
cfm = CoffeeMaker()
console = Console()
flav_choice = "-"
actual_rsrc = men.resources


while True:
    master_choice = "-"
    while master_choice != "report" and master_choice !=  "off" and master_choice !=  "espresso" and master_choice !=  "latte" and master_choice != "cappuccino":
        master_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()

    if master_choice == "off":
        console.clear()
        print("Turning off machine...")
        break
    if master_choice == "report":
        mm.report_printer(actual_rsrc)
        continue
    else:
        flav_choice = master_choice
    #HAVE TO RETURN THE ACTUAL RESOURCES VALUE AND A FLAG TO TERMINATE THE PROCESS ALSO
    if cfm.checker(flav_choice) and mm.transactioner(flav_choice): #because the object returns and holds a value itself I can pass the result of the method in the conditional
        # if src_flag == False: means the same only it is cleaner, if its not the src_flag value, then do that that's equal to if src_flag == False
        #--------------------------------------------------------------------------------------------------------------------
        #NOW I AM GOING TO INVERT OR REVERSE THE LOGIC, TO MAKE IT STRAIGHT AND THE ELSE IS CONTINUE
        cfm.coffeemaker(flav_choice)
    else:
        continue #NOT SO NECESSARY BECAUSE IF NOT (==FALSE) IT STARTS AGAIN THE LOOP

    #mm.transactioner(flav_choice) #NOW ITS NOT NECESSARY TO CARRY A PROFIT VARIABLE FOR THE ACCUMULATED PROFIT IT PERSIST WITHIN THE OBJECT CREATED BY THAT CLASS
    # The logic of the method above also returns a value for that method so if I wanted to put its value at test in a conditional it could be true without assigning it to a var




