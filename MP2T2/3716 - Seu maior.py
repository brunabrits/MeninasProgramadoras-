num = input().split()
maior = 0

def omaior(num,maior):
    for numero in num:
        numero = int(numero)
        if  numero > maior:
            maior = numero
    print(maior)
    
omaior(num,maior)
