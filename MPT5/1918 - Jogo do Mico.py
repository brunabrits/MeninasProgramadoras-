nome_jogadora = input()
lista_carta = [str(i) for i in input().split()]

if 'mico' in lista_carta:
  print(nome_jogadora,'mico!')
else:
  print(nome_jogadora,'ok')
