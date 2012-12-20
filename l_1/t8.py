a=[1,9,3,8,5,6, 10,0,20,2]

def inserir():
    num=int(input("\nDigite um número: "))
    a.append(num)

def remover():
    num=int(input("\nDigite um número: "))
    indices=[]
    for i in range(len(a)):
        if(a[i]==num):
            indices.append(i)
            
    for i in indices:
        a.remove(a[i])
        
def ordena_decrescente(a):
    aux=0
    i=0
    for i in range(len(a)):
        k=0
        while(k!=len(a)-1 ):
                if(a[i]>a[k]):
                    aux=a[i]
                    a[i]=a[k]
                    a[k]=aux
                k+=1
    return a

def ordena_crescente(a):
    a=ordena_decrescente(a)
    aux=[]
    for i in range(len(a)-1,-1,-1):
        aux.append(a[i])

    return aux

op=0
while(op!=5):
    print("\n\n***** Menu principal *****")
    print("\n    1 - Inserir um número")
    print("\n    2 - Remover um número")
    print("\n    3 - Listar em ordem decrescente")
    print("\n    4 - Listar em ordem crescente")
    op=int(input("\n  Digite o número de sua escolha: "))

    if(op==1):
        inserir()
        print("\n      Número inserido com sucesso")
    elif(op==2):
        remover()
        print("\n      Número removido com sucesso")
    elif(op==3):
        a=ordena_crescente(a)
        for b in a:
            print(b)
    elif(op==4):
        a=ordena_decrescente(a)
        for c in a:
            print(c)
    elif(op==5):
        print("\n      Saindo..")
    else:
        print("\n     Opção inexistente!")
