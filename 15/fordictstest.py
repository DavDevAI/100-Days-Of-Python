#ITERANDO SOBRE UN DICCIONARIO
lenguaje = {
    "nombre": "Python", 
    "creador": "Guido van Rossum"
}

# for elemento in lenguaje.keys(): #como en C++ solo que no debo de declarar explícitamente
#     print (elemento)

# for elemento in lenguaje.values(): #como en C++ solo que no debo de declarar explícitamente
#     print (elemento)

#ahora para que itere y devuelva 2 valores usamos el metodo items()

for llave, valor in lenguaje.items(): # es decir imprimir la llave y valor o elemento completo,  y lo devuelve como una lista de tuplas, si lo cambiamos a un elemento
    print(llave, valor)


#si queremos que lo concatene a u elemento lo devuelve como lista de tuplas

# for concat in lenguaje.items(): 
#     print(type(concat))


MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

for ingr, qty in MENU["espresso"]["ingredients"].items():
    resources[ingr] -= qty
    newres = resources

print(type(newres))
    
