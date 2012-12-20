# -*- coding: cp1252 -*-
name_prod = []
quant_init = []

print("\nDigite o nome e a quantidade inicial dos 20 produtos: ")
for i in range(20):
    name_prod.append(raw_input("\n    "+str(i+1)+" - Nome: "))
    aux = int(input("\n    "+str(i+1)+" - Quantidade inicial de estoque: "))
    while(aux<0):
        print("\nDigite uma quantidade acima de zero!")
        aux = int(input("\n    "+str(i+1)+" - Quantidade inicial de estoque: "))
        
    quant_init.append(aux)

a = 0
while(a!=-1):
    a = int(input("\nDigite o número do produto (1 a 20): (ou -1 para sair)"))
    if (a!=-1):
        if(a>0 and a<21):
            tipo = raw_input("Digite C se for compra ou V se for venda: ")
            if(tipo=='C'):
                quant = int(input("\nDigite a quantidade: "))
                if(quant>0):
                    quant_init[a-1]+=quant
                else:
                    print("\nA quantidade não pode ser negativa!")
            elif(tipo=='V'):
                quant = int(input("\nDigite a quantidade: "))
                if(quant>0 and quant<=quant_init[a-1]):
                    quant_init[a-1]-=quant
                elif(quant>quant_init[a-1]):
                    print("\nA quantidade não pode ser maior que a inicial do produto!")
                else:
                    print("\nA quantidade não pode ser negativa!")
            else:
                print("\nEste tipo de transação não existe!")
        else:
            print("\nEste número não pertence a nenhum produto!")
    else:
        print("\nSaindo...")

print("\n\nRelatóro dos status dos produtos: ")
for i in range(20):
    print("\n    Produto "+str(i+1)+": ")
    print("\n      Nome: "+name_prod[i])
    print("\n      Quantidade atual: "+str(quant_init[i]))
