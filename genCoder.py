import random

def lista_a_diccionario(lista):
    # Creamos una copia de la lista original
    lista_valores = lista[:]
    
    # Mezclamos aleatoriamente los valores de la lista
    random.shuffle(lista_valores)
    
    # Creamos el diccionario con las claves en el orden original y los valores aleatorios
    diccionario = {lista[i]: lista_valores[i] for i in range(len(lista))}
    
    return diccionario

# Lista original
listBase = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," ","¿","?","-","*","¡","!",".",",",":",";","/","(",")","#","{","}","="]

# Generamos el diccionario con la lista aleatorizada
diccionario_resultante = lista_a_diccionario(listBase)

# Guardamos el diccionario como texto simple en un archivo .txt con codificación UTF-8
with open("diccionario.txt", "w", encoding="utf-8") as file:
    file.write(str(diccionario_resultante))

print("El diccionario ha sido exportado a 'diccionario.txt' con codificación UTF-8")
