a=[]
b=[]
for k in range(2):
    print("\nPreencha a %iª matriz: "%(k+1))
    for i in range(5):
        a.append([])
        b.append([])
        for j in range(3):
            if(k==0):
                a[i].append(float(input("\n    Digite o elemento da %iª linha e da %iª coluna: "%(i+1,j+1))))
            elif(k==1):
                b[i].append(float(input("\n    Digite o elemento da %iª linha e da %iª coluna: "%(i+1,j+1))))

soma=[]
for i in range(5):
    soma.append([])
    for j in range(3):
        soma[i].append(a[i][j]+b[i][j])

print("\n\nResultado das somas das matrizes: ")
for i in range(5):
    for j in range(3):
        print(a[i][j], end="  ")
    print("\n")

print("+\n")

for i in range(5):
    for j in range(3):
        print(b[i][j], end="  ")
    print("\n")

print("=\n")

for i in range(5):
    for j in range(3):
        print(soma[i][j], end="  ")
    print("\n")
