op=4

def add_ips():
    a = int(input("Digite a quantidade de ips a serem classificados: "))

    arq = open('ips.txt','w')
    print("\n\nDigite os ips para salvá-los:")
    for i in range(a):
        b = input("\nDigite o "+str(i+1)+": ")
        arq.write(b+"\n")

    arq.close()

def verify_ips():
    arq = open('ips.txt','r')
    b=arq.readlines()
    arq.close()

    arq = open('ips_classifieds.txt','w')
    ips_validos=[]
    ips_invalidos=[]
    
    for i in range(len(b)):
        a=b[i].split(".")
        ok=1
        if(len(a)==4):
            ok=1
        else:
            ok=0
            ips_invalidos.append(b[i])
            
        if(ok!=0):
            ips=[0,0,0,0]
            for j in range(4):
                try:
                    ips[j]=int(a[j])
                except:
                    ok=0
            if(ok!=0):
                acerto=0
                for j in range(4):
                    for k in range(256):
                        if(ips[j]==k):
                            acerto+=1
                if(acerto==4):
                    ok=1
                else:
                    ok=0

                if(ok!=0):
                    ips_validos.append(b[i])
                else:
                    ips_invalidos.append(b[i])
            else:
                ips_invalidos.append(b[i])
        else:
                ips_invalidos.append(b[i])

    arq.write('Ips válidos: \n')
    arq.writelines(ips_validos)
    arq.write('\n')
    arq.write('Ips inválidos: \n')
    arq.writelines(ips_invalidos)
    arq.close()
       
while (op!=3):
    print("\n\n**** Menu ****")
    print("\n    1 - Adicionar novos ips para classificação")
    print("\n    2 - Classificar os que já estão gravados")
    op = int(input('\n  Digite o número da opção escolhida ou 3 para sair!'))

    if(op==1):
        add_ips()
    elif(op==2):
        verify_ips()
    elif(op==3):
        print("\nSaindo...")
