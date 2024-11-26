print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")
# Se le dice al usuario que ingrese el año que cursa
añoac = int(input("Ingresa el año que cursas: "))

# se coloca una lista vacia para almacenar los datos
personas = []

# Se ingresa informacion de tres personas mas 
for i in range(3):
    n= input(f"Coloca el nombre de la primera persona {i + 1}: ")
    añodn= int(input(f"Coloque el año de nacimiento {n}: "))
    edad = añoac - añodn #SE CALCULA LA EDAD    
    personas.append((n, edad))  #SE AGREGA A LA LISTA

#Se muestra el resultado
print("\nAños que cumple en el curso:")
for n, edad in personas:
    print(f"{n} cumplirá {edad} años.")