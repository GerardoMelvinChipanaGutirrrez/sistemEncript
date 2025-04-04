texto = input("texto bin:")
binario = ' '.join(format(ord(caracter), '08b') for caracter in texto)
print(binario)
