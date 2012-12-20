def carrega_filmes():
    keys=['titulo','sinopse','serie','ator principal','estado']
    arq = open("filmes.txt","r")
    list_ = arq.readlines()
    arq.close()
    
    list_dict=[]
    for i in range(len(list_)):
        aux={}
        if (list_[i]!='\n'):
            k=0
            a=list_[i].split('|')
            for j in keys:
                aux[j]=a[k]
                k+=1
               
            list_dict.append(aux)
        
    return list_dict

def cadastro():
    print("\n    Cadastro..")
    a=['titulo','sinopse','serie','ator principal','estado']

    b={}
    b['titulo'] = input('\n      Digite o título: ')
    b['sinopse'] = input('\n      Digite a sinopse: ')
    b['serie'] = input("\n      Digite a série (ouro, prata ou bronze): ")
    b['ator principal'] = input("\n      Digite o ator principal: ")
    b['estado']='disponivel'

    erro=0
    aux=""
    for i in a:
        if(b[i]!='' and b[i]!=' '):
            if(i!='estado'):
                aux+=b[i]+'|'
            else:
                aux+=b[i]+'\n'
        else:
            erro+=1

    if(erro==0):
        arq=open('filmes.txt','a')
        arq.write(aux)
        arq.close()
        print("\n      Cadastro concluído com sucesso!")
    else:
        print("\n      Cadastro impedido por conter campos em branco!")
        

def emprestimo():
    print("\n    Aluguel..")
    titulo=input('\n      Digite um título: ')
    count=0
    num=0
    msg=""
    lista=carrega_filmes()
    for i in range(len(lista)):
        if(lista[i]['titulo']==titulo):
            count+=1
            if(lista[i]['estado']=="disponivel" or lista[i]['estado']=="disponivel\n"):
                lista[i]['estado']='alugado'
                msg='\n      Aluguel realizado com sucesso.'
                num=i
            else:
                msg='\n      Filme já está alugado, aluguel não realizado.'

    if(count==0):
        msg='\n    Não foi encontrado o filme com o título procurado'
    else:
        keys=['titulo','sinopse','serie','ator principal','estado']
        aux=""
        for i in keys:
            if(i!='estado'):
                aux+=lista[num][i]+'|'
            else:
                aux+=lista[num][i]+'\n'

        l=[]
        arq=open('filmes.txt','r')
        l=arq.readlines()
        arq.close()

        l[num]=aux
        arq=open('filmes.txt','w')
        arq.writelines(l)
        arq.close()

    print(msg)

def devolucao():
    print("\n    Devolução..")
    titulo=input('\n      Digite um título: ')
    count=0
    num=0
    msg=""
    lista=carrega_filmes()
    for i in range(len(lista)):
        if(lista[i]['titulo']==titulo):
            count+=1
            if(lista[i]['estado']=='alugado' or lista[i]['estado']=='alugado\n'):
                lista[i]['estado']='disponivel'
                msg='\n      Devolução realizada com sucesso.'
                num=i
            else:
                msg='\n      Livro já está disponível, devolução não realizada.'

    if(count==0):
        msg="\n    Não foi encontrado o filme com este título! "
    else:    
        keys=['titulo','sinopse','serie','ator principal','estado']
        aux=""
        for i in keys:
            if(i!='estado'):
                aux+=lista[num][i]+'|'
            else:
                aux+=lista[num][i]+'\n'

        l=[]
        arq=open('filmes.txt','r')
        l=arq.readlines()
        arq.close()

        l[num]=aux
        arq=open('filmes.txt','w')
        arq.writelines(l)
        arq.close()

    print(msg)

def listagem_disp():
    count=0
    keys=['titulo','sinopse','serie','ator principal','estado']
    list_=carrega_filmes()
    for i in range(len(list_)):
        if(list_[i]['estado']=='disponivel' or list_[i]['estado']=='disponivel\n'):
            count+=1
            if(count==1):
                print("\n    Listagem dos que estão disponíveis..")

            print('\n      Filme de código '+str(i+1)+": ")
            for j in keys:
                print("\n        "+j+": "+list_[i][j])

    if(count==0):
        print('\n      Não há filmes disponíveis!')    
        
def listagem_ator():
    ator=input('\n    Digite o ator que deseja consultar: ')
    count=0
    list_=carrega_filmes()
    keys=['titulo','sinopse','serie','ator principal','estado']
    for i in range(len(list_)):
        if(list_[i]['ator principal']==ator):
            count+=1
            if(count==1):
                print("\n    Listagem por ator principal..")
            print('\n      Filme de código '+str(i+1)+": ")
            for j in keys:
                print("\n        "+j+": "+list_[i][j])

    if(count==0):
        print('\n      Não há filmes com o ator procurado!')
        
def busca_status():
    titulo=input('\n    Digite o título do filme que deseja consultar o status: ')
    count=0
    keys=['titulo','sinopse','serie','ator principal','estado']
    list_=carrega_filmes()
    for i in range(len(list_)):
        if( list_[i]['titulo']==titulo):
            count+=1
            if(count==1):
                print("\n    Status do filme procurado..")

            print('\n      Filme de código '+str(i+1)+": ")
            for j in keys:
                print("\n        "+j+": "+list_[i][j])
                
    if(count==0):
        print('\n      Não há filmes com o título procurado!')

def remocao():
    titulo=input('\n    Digite o título do filme que deseja remover: ')
    num=0
    count=0
    list_=carrega_filmes()
    for i in range(len(list_)):
        if( list_[i]['titulo']==titulo):
            count+=1
            num=i
            
    if(count!=0):
        l=[]
        arq=open('filmes.txt','r')
        l=arq.readlines()
        arq.close()

        l.remove(l[num])
        arq=open('filmes.txt','w')
        arq.writelines(l)
        arq.close()
        print("\n      Remoção feita com sucesso!")
    else:
        print('\n      Não há filmes com o título procurado!')
        
a=0
while(a!=8):
    print("\n\n***** Atividades da locadora \"Myuk & Lion!\" *****")
    print("\n    1 - Cadastramento")
    print("\n    2 - Aluguel")
    print("\n    3 - Devolução")
    print("\n    4 - Remoção")
    print("\n    5 - Listagem por ator")
    print("\n    6 - Listagem dos que estão disponíveis")
    print("\n    7 - Consulta do status de um filme")
    print("\n    8 - Sair")
    a=int(input('  Digite o número da operação que desejas fazer: '))

    if(a==1):
        cadastro()
    elif(a==2):
        emprestimo()
    elif(a==3):
        devolucao()
    elif(a==4):
        remocao()
    elif(a==5):
        listagem_ator()
    elif(a==6):
        listagem_disp()
    elif(a==7):
        busca_status()
    elif(a==8):
        print("\n        Saindo...")
