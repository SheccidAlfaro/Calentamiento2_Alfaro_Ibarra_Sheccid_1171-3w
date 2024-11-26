print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")
def es_bisiesto(año):
    """
    Es año bisiesto?
    """
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

# El usuario ingresa el año
año_u = int(input("Coloque un año: "))

#Llama la funsion y muestra el resultado
if es_bisiesto(año_u):
    print(f"{año_u} es un año bisiesto.")
else:
    print(f"{año_u} no es un año bisiesto.")