# Recursividad

Este es el link de este repositorio:[GitHub](https://github.com/joseluis031/Recursividad.git)

## Ejercicio de dicotonomia
```dicoto = input("¿Que numero quieres buscar en la tabla?")
def buscar(tabla,dicoto,indice):
    if dicoto == str(tabla[indice]):
        print("el numero se encuentra en la tabla")
    else:        
        if indice < (len(tabla)-1):
            indice += 1
            buscar(tabla, dicoto, indice)

buscar([0,1,2,3,4,5,7,8,10,11,12,14,15,16,18,19,20], dicoto, 0)
```

## Ejercicio de palindromos
```palabra = input("Introduce la palabra que quieras comprobar si es un palindromo: ")
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
```

## Ejercicio de la bandera
```bandera = ["N","B","B","N","A","B","B","N","B","N","N","A","N","N","B","A","A"]
print(bandera)
negro = []
blanco = []
azul = []
def ordenada(bandera):
    if len(bandera) > 0:
        color = bandera.pop(0)
        if color =="N":
            negro.append(color)
            ordenada(bandera)
        elif color == "B":
            blanco.append(color)
            ordenada(bandera)
        elif color == "A":
            azul.append(color)
            ordenada(bandera)
        else:
            ordenada = negro + blanco + azul
            print(ordenada)
    else:
            ordenada = negro + blanco + azul
            print(ordenada)
ordenada(bandera)
```
