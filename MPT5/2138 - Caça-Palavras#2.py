caca_palavra = input()
lula = input().split()

for i in lula:
  buscar = caca_palavra.find(i)
  print(i,buscar)
