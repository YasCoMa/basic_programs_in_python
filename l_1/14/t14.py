arq = open('usuarios.txt','r')
users = arq.readlines()
arq.close()

nomes=[]
taxas=[]

for i in range(len(users)):
    nomes.append("")
    taxas.append("")
    for j in range(len(users[i])):
        if(j<16):
            nomes[i]+=users[i][j]
        else:
            taxas[i]+=users[i][j]

total=0
taxas_convertidas=[]
for i in range(len(nomes)):
    taxas_convertidas.append(float(taxas[i])/(1024*1024))
    total+=taxas_convertidas[i]

taxas_convertidas_percent=[]
for i in range(len(nomes)):
    taxas_convertidas_percent.append((taxas_convertidas[i]/total)*100)

media=total/len(nomes)
v=[]
arq=open("resultado.txt",'w')
v.append("ACME Inc.                 Uso do espaço em disco pelos usuários\n")
v.append("---------------------------------------------------------------------------\n")
v.append("Nr.        Usuário        Espaço utilizado        % de uso\n")
for i in range(len(nomes)):
    v.append(str(i+1)+"        "+nomes[i]+"        %.2f MB        %2f  \n\n"%(taxas_convertidas[i],taxas_convertidas_percent[i]))
v.append("Espaço total ocupado: %.2f MB\n"%(total))
v.append("Espaço médio ocupado: %.2f MB\n"%(media))

arq.writelines(v)
arq.close()

print("Arquivo salvo com sucesso!")
