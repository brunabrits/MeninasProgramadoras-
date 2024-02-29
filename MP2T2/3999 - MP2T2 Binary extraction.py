lista= [int(i) for i in input().split()]
qtd=int(input())
copia=lista[:]
centrais=[]

while qtd > 0:
    tamanho= len(lista)
    removido=lista.pop(tamanho//2)
    centrais.append(removido)
    qtd -=1
    
print(copia)
print(centrais)
