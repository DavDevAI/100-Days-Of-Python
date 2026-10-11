from menu import Menu
MENU = Menu.MENU
resources = Menu.resources

class CoffeeMaker:


    def checker(self, actual_rsrc, flav_choice):
        # SHOULD BE CONSTANTLY CHECKING AT START AND END
        # THE ONE THAT PRINTS REPORTS AND CHHECKS RESOURCES ARE ENOUGH BEF AND AFT STEP 1 AND 2
        # If the resources are enough
        for ingr, qty in MENU[flav_choice]["ingredients"].items():  # .items me devuelve lo que hay dentro de un diccionario
            if actual_rsrc[ingr] < qty:
                print(f"Sorry there is not enough {ingr}.")
                return False

        return True

    def coffeemaker(self,flav_choice):
        # MAKES COFFE AND SUBTRACTS RESOURCES TO MAKE IT ("substracter"), could be before or after making it
        for ingr, qty in MENU[flav_choice]["ingredients"].items():
            resources[ingr] -= qty
        actual_rsrc = resources
        print(f"Here is your {flav_choice}, enjoy")
        return actual_rsrc