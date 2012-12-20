arq = open('text_1.txt','r')
a1=arq.readlines()
arq.close()

arq = open('text_2.txt','r')
a2=arq.readlines()
arq.close()

arq = open('text_1&2.txt','w')

if (len(a1)>=len(a2)):
    for i in range(len(a2)):
        arq.write(a1[i])
        
        if (i==len(a2)-1):
            arq.write(a2[i]+'\n')
        else:
            arq.write(a2[i])

    for i in range(len(a2),len(a1),+1):
        arq.write(a1[i])

    arq.close()
else:
    for i in range(len(a1)):
        if (i==len(a1)-1):
            arq.write(a1[i]+'\n')
        else:
            arq.write(a1[i])
            
        arq.write(a2[i])
        
    for i in range(len(a1),len(a2),+1):
        arq.write(a2[i])

    arq.close()

