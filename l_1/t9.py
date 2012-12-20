v1=[]
v2=[]

for i in range(2):
    print("\n\nDigite os números do "+str(i+1)+"º vetor:")
    for j in range(25):
        if(i==0):
            v1.append(int(input("\n    Digite o %iº elemento: "%(j+1))))
        if(i==1):
            v2.append(int(input("\n    Digite o %iº elemento: "%(j+1))))

print("\n\nO resultado dos vetores intercalados: ")
inter=[]
for i in range(25):
    inter.append(v1[i])
    inter.append(v2[i])

for i in inter:
    print(i)
