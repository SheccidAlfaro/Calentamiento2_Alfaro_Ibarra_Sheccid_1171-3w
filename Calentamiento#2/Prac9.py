print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practicas python")
print("")
def con_v(palabra):
    # diccionario de vocales
    cn_v = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    
    #Cuenta las vocales
    for letra in palabra.lower():  #Se convierte  la palabra a minúsculas para contar sin distinción
        if letra in cn_v:
            cn_v[letra] += 1
            
    return cn_v

#Preguntar al usuario por la palabra
palus = input("Coloca una palabra: ")

#Llamar funsion 
resultado = con_v(palus)

# Mostrar el resultado e3n pantalla
print("\n La palabra ",palus,"tiene las siguientes vocales:")
for vocal, cantidad in resultado.items():
    print(f"{vocal}: {cantidad}")