a = input("Digite seu nome: ")

def revert_with_upper(s):
    a=""
    for i in range((len(s)-1),-1,-1):
        a+=s[i].upper()

    print("Seu nome ao contrário em maiúsculas é: "+a+".")

revert_with_upper(a)
