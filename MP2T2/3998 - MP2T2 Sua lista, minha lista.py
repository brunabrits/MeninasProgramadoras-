lista= [int(i) for i in input().split()]
ordenada =[]
c=0

while c < len(lista):
    print(f'- {lista}')
    print(f'+ {ordenada}')
    remove = lista.index(min(lista))
    ordenada.append(min(lista))
    lista.pop(remove)

print(f'- {lista}')
print(f'+ {ordenada}')
