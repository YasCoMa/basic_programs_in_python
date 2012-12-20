arq = open('teste.txt','w')
cod=[1,2,3,4,5]
nome=['a','b','c','d','e']

for i in range(len(cod)):
    arq.write("Id: "+str(cod[i])+" | Nome: "+str(nome[i])+" \n")

arq.close()

arq = open('teste.txt','r')
a=arq.readlines()
for i in range(len(a)):
    b=a[i].split('|')
    print("--- "+b[0]+"---"+b[1]+" \n")

arq.close()
