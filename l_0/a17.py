s = input("Digite uma frase: ")

def remove_spaces(a):
    d=""
    for i in range(len(a)):
        if(a[i]!=' '):
            d+=a[i]
    return d

def verify_palindromo(a):
    a_original=a
    a=remove_spaces(a)
    a_reverted=""
    for i in range(len(a)-1,-1,-1):
        a_reverted+=a[i]

    if (a_reverted==a):
        print("\n\nA palavra \""+a_original+"\" é um palíndromo.")
    else:
        print("\n\nA palavra \""+a_original+"\" não é um palíndromo.")

verify_palindromo(s)
