s = input("Digite seu nome: ")

def str_decreasing(a):
    for i in range((len(a)-1),-1,-1):
        for j in range(i+1):
            print(a[j], end="")
        print("\n")
        
str_decreasing(s)
