num = float(input("Digite um número: "))

def verify_beforeOrAfter_zero (n):
    if (n>=0):
        return 'P'
    else:
        return 'N'

if (verify_beforeOrAfter_zero(num)=='P'):
    print ("\nO número %.2f é positivo."%(num))
else:
    print ("\nO número %.2f é negativo."%(num))
