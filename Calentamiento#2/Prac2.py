print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")
#Definir una funcion que tome tome la palbra mas larga de una lista de palabras
def palabra_mas_larga(lista_palabras):
    return max(lista_palabras, key=len)
#Crear lista de palabras
lista=["hola", "python", "programacion", "Alfaro", "Abarra"]
#Llamar a la funcion
print("La palabra mas larga de la lista es: ", palabra_mas_larga(lista))
print(lista) 
