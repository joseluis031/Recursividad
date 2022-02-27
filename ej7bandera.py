bandera = ["N","B","B","N","A","B","B","N","B","N","N","A","N","N","B","A","A"]
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