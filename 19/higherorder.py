#EXAMPLE FROM PREVIOUS DAYS TO SHOW HIGHER ORDER FUNCTIONS AND PASS THEM AS PARAMETERS
#EVEN MUTATING ITS NAME

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2 #IT DIVIDES AND RETURNS AS A WHOLE NUMBER IF NOT SPECIFIED A DATA CAST like round, double or int

def calculator(n1,n2,func): #I USE FUNC like a VARIABLE I dont even need pass it as a func()
    return func(n1,n2) #HERE IS THE DEFINITION OF A HIGHER ORDER FUNCTION

print(calculator(2,3, subtract))  # the function will take any other value we give to the function if always coincide with a defined function name
#CALCULATOR IS THE HIGHER OTHER FUNCTION