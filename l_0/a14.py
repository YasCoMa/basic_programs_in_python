s = input("Digite seu nome: ")

def str_increasing(a):
    for i in range(len(a)):
        for j in range(i+1):
            print(a[j], end="")

        print("\n")

str_increasing(s)
