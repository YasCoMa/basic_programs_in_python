print("Digite a seguir o valor de cada tarifa: \n")
valor = []
quant_pag = []
arrecadacao = []
for i in range(10):
    valor.append(float(input("    Tarefa " + str(i+1) + " - valor: \n")))
    quant_pag.append(0)
    arrecadacao.append(0.0)

print("\nAgora, digite o número das tarifas (1 a 10) para registrar o pagamento, quando acabar digite -1:")
op=0
while (op!=-1):
    op=int(input("\n    Número da tarifa: "))
    if (op!=-1):
        quant_pag[op-1]+=1
        arrecadacao[op-1]+=valor[op-1]

total_quantPag = 0
total_arrecadacao = 0
for i in range(10):
    total_quantPag+=quant_pag[i]
    total_arrecadacao+=arrecadacao[i]

print("\n\nQuantidade de pagamentos por tarifa: ")
for i in range(10):
    print("\n    Tarefa " + str(i+1) + ": " + str(quant_pag[i]) + ".")

print("\n\nTotal de pagamentos de tarifa: " + str(total_quantPag) + ".")

print("\n\nValor arrecadado por tarifa: ")
for i in range(10):
    print("\n    Tarefa " + str(i+1) + ": " + str(arrecadacao[i]) + ".")

print("\n\nTotal do valor arrecadado de tarifas: " + str(total_arrecadacao) + ".")
