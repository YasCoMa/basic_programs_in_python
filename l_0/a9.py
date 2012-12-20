# -*- coding: cp1252 -*-
def revert_number(st):
    st=str(st)
    a=""
    for i in range((len(st)-1),-1,-1):
        a+=st[i]

    return int(a)

a = int(input("Digite um número inteiro: "))
print("\n O reverso do número "+str(a)+" é "+str(revert_number(a))+".")
