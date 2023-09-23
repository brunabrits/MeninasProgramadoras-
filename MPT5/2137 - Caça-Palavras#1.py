caca_palavra = input()
listinha = [str(i) for i in input().split()]

if caca_palavra in listinha:
  indexc = listinha.index(caca_palavra)
  print(caca_palavra, indexc)
else:
  print('falta',caca_palavra)
