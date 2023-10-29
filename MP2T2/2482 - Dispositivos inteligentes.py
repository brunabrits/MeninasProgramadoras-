estado=input()
parado=1
movimentado=0
while estado != "f":
    if estado == "p":
        parado +=1
    elif estado == "m":
        movimentado +=1
    estado=input()

    
if parado >= movimentado:
    print("sedentário")
else:
    print("ativo")
