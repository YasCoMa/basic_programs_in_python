# -*- coding: cp1252 -*-

num = int(input("Digite um número inteiro: "))

def repeat_dif_number(num):
    for i in range(num):
        for j in range(i+1):
            print(str(j+1)+" "),
            
        print("\n")

repeat_dif_number(num)
