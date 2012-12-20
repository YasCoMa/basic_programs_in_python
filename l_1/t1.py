a = int(input("Digite a quantidade de números: "))
b = 0
nums = []

for i in range(a):
    c = int(input("Digite um número: ")) 
    b += c
    nums.append(c)

m = b/a 
print("\n A média é " + str(m) + ".")
count=0
for i in range(a):
    if nums[i]>m:
        count+=1
        if count==1:
            print("\n Número(s) que está(ão) acima da média e sua(s) respectiva(s) posição(ões):")
        print("Posição: " + str(i) + "; Número: " + str(nums[i]) + ".")
        

if count==0:
    print("Nenhum número ficou acima da média.")
