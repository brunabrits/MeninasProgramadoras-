qtd= int(input())
soma=0

while qtd != 0:
    nome=input()
    s1=int(input())
    s2=int(input())
    s3=int(input())
    s4=int(input())
    
    if s1 >= 120 and s2 >= 120 and s3 >= 120 and s4 >= 120:
        print('{} tem monitorias OK! :-)'.format(nome))
    else:
        print('{} não tem monitorias suficientes :-('.format(nome))
    qtd -=1
