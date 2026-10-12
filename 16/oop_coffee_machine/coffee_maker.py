import shared_menu as sm

#IF I LEAVE IT HERE AND I CREATE ANOTHER OBJECT MEANS ANOTHER MACHINE BOTH OBJECTS WILL SHARE THE SAME RESOURCES ONE IS GONNA SUBSTRACT AND THE ANOTHER
#REMAINS THE SAME FOR LOGICAL PORPUSES OF THIS MACHINE WE WILL NOT CREATE ANOTHER MACHINE ON THIS PROJECT HAS NO REAL LIFE SENSE
#BUT IN A SOFTWARE CONTEXT IF I CREATE ANOTHER OBJECT "MACHINE" COULD HAPPEN AND MAKE THEM RUN IN PARALLEL AND ITS GONNA CREATE A BUG OR CRASH
#BECAUSE BOTH OR MORE (THE AMOUNT OF OBJECTS THAT I COULD POSSIBLY CREATE) MACHINES OR OBJECTS ARE GONNA BE SHARING THE SAME RESOURCES
#EXAMPLE
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# a = CoffeeMaker()
# b = CoffeeMaker()
# a.coffeemaker("latte")
# b.rsc_report()    # ¿300ml or 100ml? -> nonsense


class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    def checker(self, flav_choice):
        # SHOULD BE CONSTANTLY CHECKING AT START AND END
        # THE ONE THAT PRINTS REPORTS AND CHHECKS RESOURCES ARE ENOUGH BEF AND AFT STEP 1 AND 2
        # If the resources are enough
        for ingr, qty in sm.MENU[flav_choice]["ingredients"].items():  # .items me devuelve lo que hay dentro de un diccionario
            if self.resources[ingr] < qty:
                print(f"Sorry there is not enough {ingr}.")
                return False
        return True

    def brew(self,flav_choice):
        # MAKES COFFE AND SUBTRACTS RESOURCES TO MAKE IT ("substracter"), could be before or after making it
        for ingr, qty in sm.MENU[flav_choice]["ingredients"].items():
            self.resources[ingr] -= qty
        print(f"Here is your {flav_choice}, enjoy")
        return self.resources

    def rsc_report(self):
        print(f'''
        Water: {self.resources["water"]}ml
        Milk: {self.resources["milk"]}ml
        Coffee: {self.resources["coffee"]}g     
        ''')