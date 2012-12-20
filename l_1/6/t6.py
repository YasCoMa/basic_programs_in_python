
def carrega_livros():
    keys=['titulo','autor','assunto','estado']
    arq = open("livros.txt","r")
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
    a=['titulo','autor','assunto','estado']

    b={}
    b['titulo'] = input('\n      Digite o título: ')
    b['autor'] = input('\n      Digite o autor: ')
    b['assunto'] = input("\n      Digite o assunto: ")
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
        arq=open('livros.txt','a')
        arq.write(aux)
        arq.close()
        print("\n      Cadastro concluído com sucesso!")
    else:
        print("\n      Cadastro impedido por conter campos em branco!")
        

def emprestimo():
    print("\n    Empréstimo..")
    titulo=input('\n      Digite um título: ')
    count=0
    num=0
    msg=""
    lista=carrega_livros()
    for i in range(len(lista)):
        if(lista[i]['titulo']==titulo):
            count+=1
            if(lista[i]['estado']=="disponivel"):
                lista[i]['estado']='emprestado'
                msg='\n      Empréstimo realizado com sucesso.'
                num=i
            else:
                msg='\n      Livro já está emprestado, empréstimo não realizado.'

    if(count==0):
        msg='\n    Não foi encontrado o livro com o título procurado'
    else:
        keys=['titulo','autor','assunto','estado']
        aux=""
        for i in keys:
            if(i!='estado'):
                aux+=lista[num][i]+'|'
            else:
                aux+=lista[num][i]

        l=[]
        arq=open('livros.txt','r')
        l=arq.readlines()
        arq.close()

        l[num]=aux
        arq=open('livros.txt','w')
        arq.writelines(l)
        arq.close()

    print(msg)

def devolucao():
    print("\n    Devolução..")
    titulo=input('\n      Digite um título: ')
    count=0
    num=0
    msg=""
    lista=carrega_livros()
    for i in range(len(lista)):
        if(lista[i]['titulo']==titulo):
            count+=1
            if(lista[i]['estado']=='emprestado'):
                lista[i]['estado']='disponivel'
                msg='\n      Devolução realizada com sucesso.'
                num=i
            else:
                msg='\n      Livro já está disponível, devolução não realizada.'

    if(count==0):
        msg="\n    Não foi encontrado o livro com este título! "
    else:    
        keys=['titulo','autor','assunto','estado']
        aux=""
        for i in keys:
            if(i!='estado'):
                aux+=lista[num][i]+'|'
            else:
                aux+=lista[num][i]

        l=[]
        arq=open('livros.txt','r')
        l=arq.readlines()
        arq.close()

        l[num]=aux
        arq=open('livros.txt','w')
        arq.writelines(l)
        arq.close()

    print(msg)

def listagem_emp():
    count=0
    keys=['titulo','autor','assunto','estado']
    list_=carrega_livros()
    for i in range(len(list_)):
        if(list_[i]['estado']=='emprestado'):
            count+=1
            if(count==1):
                print("\n    Listagem dos que estão emprestados..")

            print('\n      Livro de código '+str(i+1)+": ")
            for j in keys:
                print("\n        "+j+": "+list_[i][j])

    if(count==0):
        print('\n      Não há livro emprestado!')    
        
def listagem_autor():
    autor=input('\n    Digite o autor que deseja consultar: ')
    count=0
    list_=carrega_livros()
    for i in range(len(list_)):
        if(list_[i]['autor']==autor):
            count+=1
            if(count==1):
                print("\n    Listagem por autor..")
            print('\n      Livro de código '+str(i+1)+": ")
            print("\n        Título: "+list_[i]['titulo'])

    if(count==0):
        print('\n      Não há livros com o autor procurado!')
        
def listagem_assunto():
    print("\n    Listagem por assunto..")
    assunto=input('\n    Digite o assunto que deseja consultar: ')
    count=0
    keys=['titulo','autor','assunto','estado']
    list_=carrega_livros()
    for i in range(len(list_)):
        if((list_[i]['estado']=='disponivel' or list_[i]['estado']=='disponivel\n') and list_[i]['assunto']==assunto):
            count+=1
            if(count==1):
                print("\n    Listagem por assunto..")

            print('\n      Livro de código '+str(i+1)+": ")
            for j in keys:
                print("\n        "+j+": "+list_[i][j])
                
    if(count==0):
        print('\n      Não há livros com o assunto procurado!')
        
a=0
while(a!=7):
    print("\n\n***** Atividades da livraria \"Imagine!\" *****")
    print("\n    1 - Cadastramento")
    print("\n    2 - Empréstimo")
    print("\n    3 - Devolução")
    print("\n    4 - Listagem dos que estão emprestados")
    print("\n    5 - Listagem por autor")
    print("\n    6 - Listagem por assunto")
    print("\n    7 - Sair")
    a=int(input('  Digite o número da operação que desejas fazer: '))

    if(a==1):
        cadastro()
    elif(a==2):
        emprestimo()
    elif(a==3):
        devolucao()
    elif(a==4):
        listagem_emp()
    elif(a==5):
        listagem_autor()
    elif(a==6):
        listagem_assunto()
    elif(a==7):
        print("\n        Saindo...")
