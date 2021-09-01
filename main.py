
print("Loja de Tintas")
quant3=0
quant18=0.0
area=float(input("Informe o tamanho em metros quadrados: "))
arealitro=area*1/6;
#apenas latas de 18 litros
if(arealitro<=18):
    print("Sera necessario comprar apenas 1 lata de 18 litros e ira custar no total 80 reais")
elif(arealitro>18):
    resto=arealitro%18
    quant=arealitro/18
    quant = int(quant)
    if(resto==0):
        preco=80*quant
        print("Sera necessario comprar ",quant," latas de 18 litros e ira custar no total ",preco," reais")
    elif(resto!=0):
        quant=quant+1
        preco=80*quant
        print("Sera necessario comprar ",quant," latas de 18 litros e ira custar no total ",preco," reais")
#apenas latas de 3.6 litros
if(arealitro<=3.6):
    print("Sera necessario comprar apenas 1 lata de 3.6 litros e ira custar no total 80 reais")
elif(arealitro>3.6):
    resto=arealitro%3.6
    quant=arealitro/3.6
    quant = int(quant)
    if(resto==0):
        preco=25*quant
        print("Sera necessario comprar ",quant," latas de 3.6  litros e ira custar no total ",preco," reais")
    elif(resto!=0):
        quant=quant+1
        preco=25*quant
        print("Sera necessario comprar ",quant," latas de 3.6  litros e ira custar no total ",preco," reais")
#misturar latas e galões
if(arealitro<=3.6):
    print("Sera necessario comprar apenas 1 lata de 3.6 litros e ira custar no total 25 reais")
elif(arealitro<=18 and arealitro >3.6):
    print("Sera necessario comprar apenas 1 lata de 18 litros e ira custar no total 80 reais")
elif(arealitro>18):
    quant18=(arealitro)/18
    quant18=int(quant18)
    arealitro = arealitro - (quant18 *18)
    if(arealitro<=10.8):
        quant3=(arealitro/3.6)
        resto3=arealitro%3.6
        quant3=int(quant3)
        arealitro = arealitro - (quant3 *3.6)
        if(resto3!=0):
            quant3=quant3+1
    else:
        quant18=quant18 + 1
precototal=(quant18*80)+(quant3*25) #18=240 #3=25
print("Sera necessario comprar",quant18," latas de 18 litros e ",quant3," latas de 3.6 litros com o preço total de ",precototal," reais")

            
    