from menu import Menu
MENU = Menu.MENU
resources = Menu.resources

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
        for ingr, qty in MENU[flav_choice]["ingredients"].items():  # .items me devuelve lo que hay dentro de un diccionario
            if self.resources[ingr] < qty:
                print(f"Sorry there is not enough {ingr}.")
                return False

        return True

    def coffeemaker(self,flav_choice):
        # MAKES COFFE AND SUBTRACTS RESOURCES TO MAKE IT ("substracter"), could be before or after making it
        for ingr, qty in MENU[flav_choice]["ingredients"].items():
            resources[ingr] -= qty
        self.resources = resources
        print(f"Here is your {flav_choice}, enjoy")
        return self.resources