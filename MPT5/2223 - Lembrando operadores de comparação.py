a = int(input())
b = int(input())
c = int(input())
d= int(input())

print((c > a) and (c > b))
print((c > a) or (c > b))
print(c > b > a)
print(a >= b)

print("")

print ((c < a) or (c >= b))
print (c != (a+b))
print(a == b)
print(c < a)

print("")

print(b != a)
print ((c > d) or (b > a))
print ((a < b) or  (c < d))
print ((b < a) and (d > c)) 

print("")

print((not (a != c)))
print((not (d > a > b)))
print((not (c < (d + a))))
print((not (not(b > a))))

print("")

print((not (b > a) or ((d > c) and (a < b))))
print((b < a) and (d > c > a))
print((a < b < c < d) or (d >= a))
print(not (c > a) and ((d > c) and (a < b) and (c > a)))
