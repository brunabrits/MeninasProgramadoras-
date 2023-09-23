primeirapalavra = input()
segundapalavra = ''
letra = input()

while letra != '.':
  segundapalavra = segundapalavra + letra
  letra = input()
print(primeirapalavra == segundapalavra)
