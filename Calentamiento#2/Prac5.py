print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")

# el usuario coloca un numero binario
numb = input("Incerte un numero binario: ")

# Verificar asi el usuario coloca un numero binario
if all(bit in '01' for bit in numb):
    # Se convierte el numero binario a entero
    numen = int(numb, 2)
    #Mostrar el resultao en pantalla
    print(f"El número binario {numb} es igual a {numen} en decimal.")
else:
    print("No es numero binario")