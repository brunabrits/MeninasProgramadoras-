a,b,c=map(int,input().split())

def segundograu(a,b,c):
    delta= b **2 - 4*a*c
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return 0


print(segundograu(a,b,c))
