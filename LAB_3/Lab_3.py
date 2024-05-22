# Presentar el tipo de dato de cadena

myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# Trabajar con concatenación de cadenas

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Trabajar con cadenas de entrada

name = input(" What is your name? ")
print(name)

# Dar formato a las cadenas de salida

color = input(" What is your favorite color? ")
animal = input(" What is your favorite animal? ")

print("{}, you like a {} {}!".format(name,color,animal))

