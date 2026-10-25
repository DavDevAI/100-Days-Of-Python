from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from rich.console import Console

mm = MoneyMachine()
cfm = CoffeeMaker()
console = Console()
flav_choice = "-"


while True:
    master_choice = "-"
    while master_choice != "report" and master_choice !=  "off" and master_choice !=  "espresso" and master_choice !=  "latte" and master_choice != "cappuccino":
        master_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()

    if master_choice == "off":
        console.clear()
        print("Turning off machine...")
        break
    if master_choice == "report":
        cfm.rsc_report()
        mm.profit_report()
        continue
    else:
        flav_choice = master_choice
    #HAVE TO RETURN THE ACTUAL RESOURCES VALUE AND A FLAG TO TERMINATE THE PROCESS ALSO
    if cfm.checker(flav_choice) and mm.transactioner(flav_choice): #because the object returns and holds a value itself I can pass the result of the method in the conditional
        # if src_flag == False: means the same only it is cleaner, if its not the src_flag value, then do that that's equal to if src_flag == False
        #--------------------------------------------------------------------------------------------------------------------
        #NOW I AM GOING TO INVERT OR REVERSE THE LOGIC, TO MAKE IT STRAIGHT AND THE ELSE IS CONTINUE
        cfm.brew(flav_choice)
    else:
        continue #NOT SO NECESSARY BECAUSE IF NOT (==FALSE) IT STARTS AGAIN THE LOOP

    #mm.transactioner(flav_choice) #NOW ITS NOT NECESSARY TO CARRY A PROFIT VARIABLE FOR THE ACCUMULATED PROFIT IT PERSIST WITHIN THE OBJECT CREATED BY THAT CLASS
    # The logic of the method above also returns a value for that method so if I wanted to put its value at test in a conditional it could be true without assigning it to a var


#COMO VISTO EN LA CLASE DE UNIV PYTHON Y SOBRE LOS ATRIBUTOS DE CLASE Y DE ATRIBUTOS DE INSTANCIA Y OBJETO  AQUI POR MOTIVOS PRACTICOS
# NO SE VA A CREAR MAS DE 1 OBJETO PORQUE NO ES COMO QUE EN LA VIDA REAL PODAMOS CREAR 2 MAQUINAS DE CAFE EN UNA, PERO EN SOFTWARE A ESE NIVEL SI SE PODRÍA
# POR LO QUE POR ESO SE CREO UN SHARED MENU, PARA QUE NO IMPORTE EL NUMERO DE OBJETOS CREADOS NO MUTEN A UNA FUENTE DE RECURSOS EN COMUN

#IGUAL PARA EFECTOS LOGICOS Y FISICOS REPRENSENTATIVOS DE ESTE SISTEMA SOLO SE CREA UN OBJETO QUE ES UNA SOLA MAQUINA DE CAFE Y COMO ES SOLO 1 OBJETO O UNA INTANCIA
# PUES SE COMPARTE EN LOS ATRIBUTOS DE OBJETO LOS QUE ESTAN EN EL CONSTRUCTOR QUE SON self.atributo y entre ellos se comparte entre ellos se acumula y entre ellos se
# retorna sin explicitamente asginar un valor porque el objeto en si mismo carrea consigo mismo esos atributos y se va a acumulando ya que justo para efectos practicos
# si creo otro objeto la mutacion de sus parametros internos justamente se queda contenida dentro de ese mismo objeto y no se comparte con los del otro objeto para
# que no haya interferencia y justo ese objeto es una instancia o "clonacion" de lo que representa esa clase que estan clonando y modificando o mas bien instanciando y modificando
# usandola como una plantilla reciclable en la que cada objeto tiene sus propios atributos y metodos

