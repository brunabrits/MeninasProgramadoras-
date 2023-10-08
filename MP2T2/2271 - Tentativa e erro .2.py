num= int(input())
palpite= int(input())

while palpite != num:
    if palpite < num:
        print('maior')
        palpite= int(input())
    elif palpite > num:
        print('menor')
        palpite= int(input())
print('igual')
 
