lista = []

entrada1 = int(input("Digite um numero: "))
lista.append(entrada1)
entrada2 = int(input("Digite um numero: "))
lista.append(entrada2)
entrada3 = int(input("Digite um numero: "))
lista.append(entrada3)
entrada4 = int(input("Digite um numero: "))
lista.append(entrada4)
entrada5 = int(input("Digite um numero: "))
lista.append(entrada5)

contadorPar = 0
contadorImpar = 0

for entrada in lista: 
    if entrada % 2 == 0:
        contadorPar = contadorPar + 1
    else:
        contadorImpar = contadorImpar + 1

print(f"Voce digitou {contadorPar} números pares e {contadorImpar} números ímpares.")

