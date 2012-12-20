n = int(input("Digite o tamanho final: "))

print((" "*((n*n)-3))+"/\\", end="\n")
for j in range(n):
    o = n-(j)
    print(" "*((o*n)-3), end="")
        
    for i in range(((j+1)*(-1)), j+2):
        if(i!=0):
            if(i<0):
                print(str(i*(-1)), end="()")
            else:
                print("()"+str(i), end="")
        else:
            print("||", end="")
    print("\n")


