# Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene.
 ## El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.


def principal():
    phrase = input("Please enter a phrase : ")
    total = 1
    i = 0
    while(i < len(phrase)):
        if(phrase[i] == ' '):
            total += 1
        i += 1
    print("Total Number of Words in this String = ", total)
