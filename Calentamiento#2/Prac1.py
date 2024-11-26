print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")
#Definir una funcion que devuelva el numero mas grande de una lista sin necesidad de utilizar la funcion max()
def maximo(lista):
    if not lista:  # Verifica si la lista está vacía
        return None  # O puedes lanzar una excepción si prefieres
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo  # Devuelve el valor máximo encontrado

#Poner a prueba la funcion
lista = [23, 45, 34, 98, 124, 12]
resultado = maximo(lista)
print(lista)
print("El valor máximo es:", resultado)