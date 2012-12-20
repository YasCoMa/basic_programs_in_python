taxa = float(input("Digite o valor do imposto sobre o produto (em %): "))
custo = float(input("Digite o valor do preço de custo do produto: "))

def sum_taxe_to_price (t,c):
    print("O novo valor do preço é %.2f."%((c+((t/100)*c))))

sum_taxe_to_price(taxa,custo)
