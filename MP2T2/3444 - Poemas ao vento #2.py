poema= input().lower()
subs= [',','.','""',"''"]
for ponto in subs:
  poema= poema.replace(ponto,'')
  lista= poema.split()
dicionario={}

for palavra in lista:
  if palavra in dicionario:
    dicionario[palavra] +=1
  else:
    dicionario[palavra] =1
print(dicionario)

consulta=input().lower()
if consulta in dicionario:
  result = dicionario[consulta]
  print(result)
else:
  print('%s não encontrada' % consulta)
