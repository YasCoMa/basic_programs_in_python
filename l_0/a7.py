# -*- coding: cp1252 -*-
quant = 0
soma = 0
val_prest = -1

def add_taxes_by_delay(prest,q_dias_delay):
    if (q_dias_delay>0):
        prest=prest+(prest*0.03)+(prest*(0.001*q_dias_delay))

    return prest



while (val_prest!=0):
    print("\n\n***** Programa para pagamento de presta��es *****")
    print("\nDigite zero(0) no valor da presta��o para sair!")

    val_prest = float(input("Digite o valor da presta��o: "))
    q_atraso = int(input("Digite a quantidade de dias de atraso: "))

    if (val_prest>0):
        quant+=1
        val_prest=add_taxes_by_delay(val_prest,q_atraso)
        print("O valor a ser pago � "+str(val_prest)+".")
        soma+=val_prest

print("\n\n***** Relat�rio de pagamentos *****")
print("\n    Quantidade de pagamentos: "+str(quant)+".")
print("\n    Soma de todos os pagamentos: "+str(soma)+".")
