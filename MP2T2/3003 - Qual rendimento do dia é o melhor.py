numeros=[]
while numeros.count('0') != 1:
  num = input()
  numeros.append(num)

print(max(numeros))
