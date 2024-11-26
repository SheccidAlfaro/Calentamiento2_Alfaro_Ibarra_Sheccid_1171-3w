print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")
# Define una lista de nombres
noms = ["Sheccid", "Aleshka", "Jazmin", "Luis", "Jose", "Luz", "Sol", "Alma", "Julian", "Lucas"]

#El usuario ingresa una letra
letra = input("Coloca una letra para buscar el nombre que empiece con esa letra: ").lower()

# Contar los nombres
cn_nm = sum(1 for nom in noms if nom.lower().startswith(letra))

#Mostrar el resultado en pantalla 
print(f"\nEstos son los nombres encontrados: '{letra}': {cn_nm}")