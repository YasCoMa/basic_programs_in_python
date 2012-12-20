print("Digite abaixo o nome dos aparelhos da loja: ")
nomes = []
quant_vendas = []
for i in range(15):
    nomes.append(input("\n    Aparelho " + str(i+1) + ":"))
    quant_vendas.append(0.0)

op=0
while (op!=4):
    print("\n\nMenu principal")
    print("\n    1 - Vendas")
    print("\n    2 - Totais")
    print("\n    3 - Mais vendido")
    print("\n    4 - Sair");
    op=int(input("\n  Número da opção: "))

    if (op==1):
        print("\n\nDigite o código e a quantidade vendida de cada aparelho, para terminar digite -1 no código:")
        a=int(input("\n    Código:"))
        if (a!=-1):
            if(a>=1 and a<=15):
                quant_vendas[a-1]+=int(input("\n    Quantidade vendida:"))
            else:
                print("\nNão existe produto com este código!")
                
        while (a!=-1):
            a=int(input("\n    Código:"))
            if (a!=-1):
                if(a>=1 and a<=15):
                    quant_vendas[a-1]+=int(input("\n    Quantidade vendida:"))
                else:
                    print("\nNão existe produto com este código!")

    elif (op==2):
        print("\n\nTotais de vendas dos aparelhos:")
        for i in range(15):
            print("\n    Aparelho " + str(i+1) + ": " + str(quant_vendas[i]) + ".")

    elif (op==3):
        ma=quant_vendas[0]
        for i in range(15):
            if (quant_vendas[i]>ma):
                ma=quant_vendas[i]

        print("\n\nAparelhos mais vendidos: ")
        for i in range(15):
            if (quant_vendas[i]==ma):
                print("\n    " + str(nomes[i]))
