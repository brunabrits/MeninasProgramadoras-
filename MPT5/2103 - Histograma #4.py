listinha =[int(i) for i in input().split()]

menor = min(listinha)
maior = max  (listinha)

for i in range(menor, maior+1):
  contando = listinha.count(i)
  if contando >= 1:
     print(i,contando)
soma = sum (listinha)
print(soma)
