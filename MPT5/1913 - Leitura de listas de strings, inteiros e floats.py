letra = input()

if letra == 's':
 s = [str (s) for s in input().split()]
 print(s)

elif letra =='f':
  f = [int (f) for f in input().split()]
  print(f)

else:
  n = [float (n) for n in input().split()]
  print(n)
