import ast  # Para convertir el texto en un diccionario

# Paso 1: Cargar el diccionario desde el archivo
with open("diccionario.txt", "r", encoding="utf-8") as file:
    # Leemos el contenido del archivo y lo convertimos a un diccionario
    diccionario = ast.literal_eval(file.read())

# Paso 2: Crear un diccionario invertido para la decodificación
# Convertimos los valores del diccionario a cadenas para evitar problemas con números
diccionario_invertido = {str(v): k for k, v in diccionario.items()}

# Paso 3: Solicitar el texto codificado (que queremos decodificar)
entradaText = input("INGRESA TEXTO A DECODIFICAR: \n")

# Paso 4: Crear el texto decodificado usando el diccionario invertido
texto_decodificado = ""
for letra in entradaText:
    if letra in diccionario_invertido:
        # Reemplazamos el valor por la clave en el diccionario invertido
        texto_decodificado += diccionario_invertido[letra]
    else:
        # Si el valor no está en el diccionario, dejamos el carácter tal como está
        texto_decodificado += letra

# Paso 5: Imprimir el texto decodificado
print("\nTexto decodificado:")
print(texto_decodificado)
