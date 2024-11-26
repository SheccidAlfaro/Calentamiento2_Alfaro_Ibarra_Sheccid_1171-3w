print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")
# Lista vacia de edades
ed = []

# El usuario ingresa la cantidad de 10 edades
for i in range(10):
    edad = int(input(f"Ingrese la edad {i + 1}: "))
    ed.append(edad)  #Se agraga la edad en la lista 

# Se convierte a tupla 
tup_ed = tuple(ed)

# Se cuenta la cantidad de edades mayores a 20
supa20 = sum(1 for edad in tup_ed if edad > 20)

#Se muestra resultado en pantalla 
print(f"\nCantidad de personas con edades superiores a 20: {supa20}")