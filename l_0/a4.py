num = float(input("Digite um n�mero: "))

def verify_beforeOrAfter_zero (n):
    if (n>=0):
        return 'P'
    else:
        return 'N'

if (verify_beforeOrAfter_zero(num)=='P'):
    print ("\nO n�mero %.2f � positivo."%(num))
else:
    print ("\nO n�mero %.2f � negativo."%(num))
