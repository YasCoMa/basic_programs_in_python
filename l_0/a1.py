#--Print Number same Number of Time as Number

num = int(input("Digite um número inteiro: "))

def repeat_same_number(num):
    for i in range(num):
        for j in range(i+1):
            print(str(i+1)+" "),
            
        print("\n")

repeat_same_number(num)
