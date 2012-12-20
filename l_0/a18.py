op=0

while (op!=6):
    print("\n***** Menu de produtos *****")
    print("\n    1: Maiô Speedo - R$ 320.00")
    print("\n    2: Touca hammerhead - R$ 18.00")
    print("\n    3: Óculos Speedo - R$ 27.00")
    print("\n    4: Tapa ouvido - R$ 8.00")
    print("\n    5: Pé de pato - R$ 86.00")
    op = int(input("\n  Digite o número (1 a 5) do produto que desejas comprar (ou digite 6 para sair): "))

    if(op==1):
        val=320.0
    elif(op==2):
        val=18.0
    elif(op==3):
        val=27.0
    elif(op==4):
        val=8.0
    elif(op==5):
        val=86.0

    if(op!=6):    
        sm=0.0
        while(sm<val):
            print("\n Você já inseriu R$ "+str(sm)+" de R$ "+str(val)+".")
            v=float(input("Insira uma moeda: "))
            if(v==200 or v==100 or v==50 or v==20 or v==10 or v==5 or v==1):
                sm+=v
            else:
                print("\nInsira uma moeda válida!")

        troco_original=sm-val
        troco=troco_original
        
        mo=[200,100,50,20,10,5,1]
        m=[0,0,0,0,0,0,0]
        while(troco>0.0):
            for i in range(len(mo)):
                if(troco>=mo[i]):
                    m[i]+=1
                    troco-=mo[i]
                    break
        
        if(troco_original==0):
            print("\nVocê não tem troco!")
        else:
            print("\nSeu troco é de R$ "+str(troco_original)+".")
            print("\nRetire as moedas referentes ao seu troco: ")
            for i in range(len(m)):
                if(m[i]!=0):
                    print("\n "+str(m[i])+ " moeda(s) de R$ "+str(mo[i]))
