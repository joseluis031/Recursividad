palabra = input("Introduce la palabra que quieras comprobar si es un palindromo: ")
i = "aeoiUAEOIU"
palabra = palabra.lower()
palabra = palabra.replace(" "," ")
L = list(palabra)
Lista = list(reversed(palabra))

def palindromo(palabra):
    if len(palabra) < 1:
        print(palabra, "palindromo!!")
    else:
        if palabra[0] == palabra[-1]:
            palindromo(palabra[1:-1])
        else:
            print(palabra,"no es un palindromo")
palindromo(palabra)