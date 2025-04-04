import ast  # Para convertir el texto en un diccionario

# Paso 1: Cargar el diccionario desde el archivo
with open("diccionario.txt", "r", encoding="utf-8") as file:
    # Leemos el contenido del archivo y lo convertimos a un diccionario
    diccionario = ast.literal_eval(file.read())

# Paso 2: Solicitar el texto a codificar
entradaText = input("INGRESA TEXTO A CODIFICAR: \n")

# Paso 3: Crear el texto codificado usando el diccionario
texto_codificado = ""

for letra in entradaText:
    if letra in diccionario:
        # Si la letra está en el diccionario, la reemplazamos por su valor
        # Aseguramos que el valor sea convertido a string
        texto_codificado += str(diccionario[letra])
    else:
        # Si la letra no está en el diccionario (como los números o caracteres especiales),
        # la dejamos tal cual
        texto_codificado += letra

# Paso 4: Imprimir el texto codificado
print("\nTexto modificado:")
print(texto_codificado)
