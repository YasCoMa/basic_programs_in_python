print("***** Soma de três argumentos *****\n")
n1 = float(input("1º número: "))
n2 = float(input("2º número: "))
n3 = float(input("3º número: "))

def sum_three_numbers (n1,n2,n3):
    print("A soma de %.2f, %.2f e %.2f é %.2f."%(n1,n2,n3,(n1+n2+n3)))

sum_three_numbers(n1,n2,n3)
