from menu import Menu
DENOMINATIONS = Menu.DENOMINATIONS
MENU = Menu.MENU

class MoneyMachine:

    #JUSTO COMO SE VIO EN LA CLASE DE UNIV PYTHON AUNQUE EXISTEN METODOS DE INSTANCIA Y DE CLASE AQUI COMO ESTOY LIDIANDO CON
    #OBJETOS DE INSTANCIA PORQUE SIMPLEMENTE ESTOY INSTANCIANDO SI LLEVAN SELF, AUNQUE TRAIGAN EL MISMO NOMBRE NO HAY QUE HACER UN PASE DE REFERENCIA O PARAMETRO COMO
    #TAL PARA ESO EXISTE EL SELF
    def coin_totalgetter(self):

        # GETS AND PROCESS COINS
        print("Please insert coins\n")
        e_quarters = int(input("How many quarters?: \n")) * DENOMINATIONS["quarters"]
        e_dimes = int(input("How many dimes?: \n")) * DENOMINATIONS["dimes"]
        e_nickles = int(input("How many nickels?: \n")) * DENOMINATIONS["nickels"]
        e_pennies = int(input("How many pennies?: \n")) * DENOMINATIONS["pennies"]
        e_total = e_quarters + e_dimes + e_nickles + e_pennies
        return e_total


    def validator(self, e_total, flav_choice):
        # CHECKS THAT THE MONEY OR COIN TRANSACTION IS SUCCESFUL
        # TO CHECK IF ALL THE COINS ENTERED ARE ENOUGH TO FILL THE LOWEST PRICE TO EXECUTE A FLAVOR AT ALL OR EXECUTE THE TASK
        # TO CHECK AND ASSIGN CHANGE DEPENDING ON THE INPUTED AMOUNT AND ITS CORRESPONDING FLAVOR CHOSEN

        flav_cost = MENU[flav_choice]["cost"]
        if e_total < flav_cost:
            return False
        return True


    def transactioner(self, profit, e, flav_choice):
        drink_cost = MENU[flav_choice]["cost"]
        if e >= drink_cost:
            change = round(e - drink_cost, 2)
            print(f"Here is ${change} in change")
            profit += drink_cost

        return profit

    def report_printer(self, actual_rsrc, profit):
        # PRINTS THE REPORT NO MATTER WHAT IS THE CURRENT STATE, SHOULD REACT TO ON-GOING CHANGES
        # COULD BE AFTER, DURING AND BEFORE THE RESOURCES ARE BEING SUBSTRACTED
        # NEED TO GENERATE AN AUXILIAR RESOURCES DATA STRUCTURE WHICH IS THE ONE THAT IS GONA BE MUTATING DURING THE EXECUTION
        print(f'''
        Water: {actual_rsrc["water"]}ml
        Milk: {actual_rsrc["milk"]}ml
        Coffee: {actual_rsrc["coffee"]}g     
        Earned Money: ${profit}
        ''')

