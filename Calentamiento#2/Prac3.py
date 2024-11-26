print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")

def filtrar_Palabra(lista):
    lista_filtrada = []
    for palabra in lista:
        if len(palabra) > 4:
            lista_filtrada.append(palabra)
            return lista_filtrada

#Llenar la lista con palabras
palabras =["hola", "ojo","hilo", "Sheccid", "Alfaro", "Ibarra"]
print(palabras)
print("Lista modificada:" ,filtrar_Palabra(palabras))
