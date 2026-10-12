import shared_menu as sm

class MoneyMachine:

    DENOMINATIONS = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    #JUSTO COMO SE VIO EN LA CLASE DE UNIV PYTHON AUNQUE EXISTEN METODOS DE INSTANCIA Y DE CLASE AQUI COMO ESTOY LIDIANDO CON
    #OBJETOS DE INSTANCIA PORQUE SIMPLEMENTE ESTOY INSTANCIANDO SI LLEVAN SELF, AUNQUE TRAIGAN EL MISMO NOMBRE NO HAY QUE HACER UN PASE DE REFERENCIA O PARAMETRO COMO
    #TAL PARA ESO EXISTE EL SELF

    def __init__(self):
        self.profit = 0
        self.e_total = 0
        #IF I wanted to MAKE IT PRIVATE WOULD BE:
        #self._profit = profit #in case it comes from outside

    def coin_totalgetter(self):
        # GETS AND PROCESS COINS
        print("Please insert coins\n")
        self.e_total = 0
        for coin in self.DENOMINATIONS:
           self.e_total += int(input(f"How many {coin}?: \n")) * self.DENOMINATIONS[coin]
        return self.e_total


    def validator(self, flav_choice):
        # CHECKS THAT THE MONEY OR COIN TRANSACTION IS SUCCESFUL
        # TO CHECK IF ALL THE COINS ENTERED ARE ENOUGH TO FILL THE LOWEST PRICE TO EXECUTE A FLAVOR AT ALL OR EXECUTE THE TASK
        # TO CHECK AND ASSIGN CHANGE DEPENDING ON THE INPUTED AMOUNT AND ITS CORRESPONDING FLAVOR CHOSEN
        flav_cost = sm.MENU[flav_choice]["cost"]
        if self.e_total < flav_cost:
            return False
        return True


    def transactioner(self, flav_choice):
        drink_cost = sm.MENU[flav_choice]["cost"]
        self.coin_totalgetter()
        if self.validator(flav_choice):
            if self.e_total >= drink_cost:
                change = round(self.e_total - drink_cost, 2)
                print(f"Here is ${change} in change")
                self.profit += drink_cost
                #I RESTART e entered which is e_total here not in the main loop
        else:
            print("Sorry, not enough money to complete the transaction. Money refunded.")
            return False
        return self.profit

    def profit_report (self):
        # PRINTS THE REPORT NO MATTER WHAT IS THE CURRENT STATE, SHOULD REACT TO ON-GOING CHANGES
        # COULD BE AFTER, DURING AND BEFORE THE RESOURCES ARE BEING SUBSTRACTED
        # NEED TO GENERATE AN AUXILIAR RESOURCES DATA STRUCTURE WHICH IS THE ONE THAT IS GONA BE MUTATING DURING THE EXECUTION
        print(f"Earned Money: ${self.profit}")

