# -*- coding: cp1252 -*-

def quant_digito(n):
    print("A quantidade de dígitos do número "+str(n)+" é "+str(len(str(n)))+".")

num = int(input("Digite um número inteiro: "))
quant_digito(num)
