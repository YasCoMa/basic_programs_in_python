# -*- coding: cp1252 -*-

num = int(input("Digite um n�mero inteiro: "))

def repeat_same_number(num):
    for i in range(num):
        for j in range(i+1):
            print(str(i+1)+" "),
            
        print("\n")

repeat_same_number(num)
