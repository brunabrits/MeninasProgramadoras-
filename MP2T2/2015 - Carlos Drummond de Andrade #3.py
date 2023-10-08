texto = []
texto.append(input())

while texto[-1] != 'CDA 1942':
    texto.append(input())
    if texto[0] == "":
        texto.pop(0)
    elif texto[-1] == "":
        texto.pop(-1)
    
    
      
print(len(texto)-1)
