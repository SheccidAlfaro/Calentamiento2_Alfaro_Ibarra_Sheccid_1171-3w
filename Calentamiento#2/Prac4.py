print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")
# Pedir al usuario que coloque una cadena de texto
cadena = input("Coloque una cadena de texto: ")
print("")
print("La cadena ingresada es:", cadena)

# Verificar cuántas letras mayúsculas tiene la cadena
contador_mayusculas = 0

for letra in cadena:
    if letra.isupper():
        contador_mayusculas += 1

print("La cantidad de letras mayúsculas es:", contador_mayusculas)