l = int(input("Digite a quantidade de linhas: "))
c = int(input("Digite a quantidade de colunas: "))

def draw_retangle(l,c):
    if((l>=1 and l<=20) and (c>=1 and c<=20)):
        for i in range(l):
            for j in range(c):
                if((i==0 and j==0) or (i==l-1 and j==0)):
                    if(c==1):
                        print("*\n")
                    else:
                        print("*", end=" ")
                    

                elif((i==0 and j==c-1) or (i==l-1 and j==c-1)):
                    print("*\n")
                   
                elif((i==0 and j!=0) or (i==l-1 and j!=c-1)):
                    print("-", end=" ")

                elif((i!=0 or i!=l-1) and (j!=0 and j!=c-1)):
                    print(" ", end=" ")
                    
                elif((i!=0 or i!=l-1) and j==0):
                    if(c==1):
                        print("|\n")
                    else:
                        print("|", end=" ")
                        
                elif((i!=0 or i!=l-1) and j==c-1):
                    print("|\n")
    else:
        print("Os valores para as linhas e colunas devem estar entre 1 e 20.")
'''
'''
draw_retangle(l,c)
