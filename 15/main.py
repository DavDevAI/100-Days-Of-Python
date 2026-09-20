MENU = {   #this one is UPPER case because although is global we want it to be INMUTABLE
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {   #this one is lower case because although is global we want it to be mutable
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

DENOMINATIONS = {  #also this ones i want them fixed
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


# ITS A STATE MACHINE AND EACH STATE IS A FUNCTION


def checker(actual_rsrc, flav_choice):
    # SHOULD BE CONSTANTLY CHECKING AT START AND END
    # THE ONE THAT PRINTS REPORTS AND CHHECKS RESOURCES ARE ENOUGH BEF AND AFT STEP 1 AND 2
    #If the resources are enough
    for ingr, qty in MENU[flav_choice]["ingredients"].items():
        if actual_rsrc[ingr] < qty:
            print(f"Sorry there is not enough {ingr}.")
            return False

    return True



def report_printer(actual_rsrc, profit):
    # PRINTS THE REPORT NO MATTER WHAT IS THE CURRENT STATE, SHOULD REACT TO ON-GOING CHANGES
    # COULD BE AFTER, DURING AND BEFORE THE RESOURCES ARE BEING SUBSTRACTED
    # NEED TO GENERATE AN AUXILIAR RESOURCES DATA STRUCTURE WHICH IS THE ONE THAT IS GONA BE MUTATING DURING THE EXECUTION
    print(f'''
    Water: {actual_rsrc["water"]}ml
    Milk: {actual_rsrc["milk"]}ml
    Coffee: {actual_rsrc["coffee"]}g     
    Earned Money: ${profit}
    ''')


def coin_totalgetter():

    # GETS AND PROCESS COINS
    print("Please insert coins\n")
    e_quarters = int(input("How many quarters?: \n")) * DENOMINATIONS["quarters"]
    e_dimes = int(input("How many dimes?: \n")) * DENOMINATIONS["dimes"]
    e_nickles = int(input("How many nickels?: \n")) * DENOMINATIONS["nickels"]
    e_pennies = int(input("How many pennies?: \n")) * DENOMINATIONS["pennies"]
    e_total = e_quarters + e_dimes + e_nickles + e_pennies
    return e_total


def validator(e_total, flav_choice):
    # CHECKS THAT THE MONEY OR COIN TRANSACTION IS SUCCESFUL
    # TO CHECK IF ALL THE COINS ENTERED ARE ENOUGH TO FILL THE LOWEST PRICE TO EXECUTE A FLAVOR AT ALL OR EXECUTE THE TASK
    # TO CHECK AND ASSIGN CHANGE DEPENDING ON THE INPUTED AMOUNT AND ITS CORRESPONDING FLAVOR CHOSEN

    flav_cost = MENU[flav_choice]["cost"]
    if e_total < flav_cost:
        return False
    return True


def transactioner(profit, e, flav_choice):
    drink_cost = MENU[flav_choice]["cost"]
    if e >= drink_cost:
        change = round(e - drink_cost, 2)
        print(f"Here is ${change} in change")
        profit += drink_cost

    return profit


def coffeemaker(flav_choice):
    # MAKES COFFE AND SUBTRACTS RESOURCES TO MAKE IT ("substracter"), could be before or after making it
    for ingr, qty in MENU[flav_choice]["ingredients"].items():
        resources[ingr] -= qty
    actual_rsrc = resources
    print(f"Here is your {flav_choice}, enjoy")
    return actual_rsrc

flav_choice = "-"
actual_rsrc = resources
profit = 0

while True:
    master_choice = "-"
    while master_choice != "report" and master_choice !=  "off" and master_choice !=  "espresso" and master_choice !=  "latte" and master_choice != "cappuccino":
        master_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()

    # Turn off the Coffee Machine by entering “ off ” to the prompt.
    # THIS COULD BE HERE IN THE MAIN LOOP ACTING AS A DO-WHILE, WHILE IF OR SWITCH STATEMENT
    # TO CHECK IF ANY OTHER WORD DIFFERENT THAN THE COFFE FLAVORS ARE INPUTED TO CATCH THE ERROR
    # BUT I ALSO NEED TO ALWAYS CHECK FOR THE SECRET WORDS SUSCH AS 'REPORT' THAT IS THE STATUS OF THE MACHINE'S RESOURCES
    # AND THE OFF WHICH FINISHES THE WHOLE PROCESS OR THE WHOLE LOOP OF THE STATE MACHINE OF THE COFFE MACHINE

    if master_choice == "off":
        print("Turning off machine...")
        break
    if master_choice == "report":
        report_printer(actual_rsrc, profit)
        continue
    else:
        flav_choice = master_choice
    e = 0
    src_flag = checker(actual_rsrc,flav_choice) #HAVE TO RETURN THE ACTUAL RESOURCES VALUE AND A FLAG TO TERMINATE THE PROCESS ALSO
    if not src_flag: # if src_flag == False: means the same only it is cleaner, if its not the src_flag value, then do that thats equal to if src_flag == False
        continue
    e = coin_totalgetter()
    c_flag = validator(e, flav_choice)
    if not c_flag:
        print("Sorry, not enough money to complete the transaction. Money refunded.")
        continue
    profit = transactioner(profit, e, flav_choice)
    actual_rsrc = coffeemaker(flav_choice)





