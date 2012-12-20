exit=1

def convert_brazilian_hour (num1, num2):
    if (num1>=25 or num2>59 or num2<0):
        print ("Hora ou minuto com valores inválidos.")
    else:
        if (num1>12 and num1<=24):
            print("Hora internacional: "+str(num1-12)+":"+str(num2)+" p.m.")
        elif (num1<12):
            print("Hora internacional: "+str(num1)+":"+str(num2)+" a.m .")

while (exit>0):
    print("\n\n***** Conversão de apresentaçao de hora brasileira para internacional *****")
    print("\n Para sair digite um número negativo")

    num1 = int(input("Hora: "))
    if (num1>0):
        num2 = int(input("Minuto: "))
        convert_brazilian_hour(num1, num2)
    else:
        exit=num1
    

