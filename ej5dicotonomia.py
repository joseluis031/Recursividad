dicoto = input("¿Que numero quieres buscar en la tabla?")
def buscar(tabla,dicoto,indice):
    if dicoto == str(tabla[indice]):
        print("el numero se encuentra en la tabla")
    else:        
        if indice < (len(tabla)-1):
            indice += 1
            buscar(tabla, dicoto, indice)

buscar([0,1,2,3,4,5,7,8,10,11,12,14,15,16,18,19,20], dicoto, 0)