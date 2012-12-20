a=[]
def inserir_pilha():
    num=int(input("\n    Digite um número: "))
    a.append(num)
    print("\n    Número inserido com sucesso.")
    
def remover_pilha():
    a.pop(len(a)-1)
    print("\n    Número removido com sucesso.")
    
def listagem_pilha():
    for i in range(len(a)-1,-1,-1):
        print(a[i])

op=0
while(op!=4):
    print("***** Menu Principal *****")
    print("\n    1 - Inserir na pilha")
    print("\n    2 - Remover na pilha")
    print("\n    3 - Listar pilha")
    print("\n    4 - Sair")
    op=int(input("\n  Digite o número de sua escolha: "))

    if(op==1):
        inserir_pilha()
    elif(op==2):
        remover_pilha()
    elif(op==3):
        listagem_pilha()
    elif(op==4):
        print("\n    Saindo..")
    else:
        print("\n    Opção inexistente!")
