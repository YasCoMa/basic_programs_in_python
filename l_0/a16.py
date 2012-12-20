s = input("Digite uma frase: ")

def count_space(a):
    c=0
    for i in range(len(a)):
        if(a[i]==' '):
            c+=1
    return c

def count_vowel(d):
    v=[0,0,0,0,0]
    for i in range(len(d)):
        if(d[i]=='a' or d[i]=='A'):
            v[0]+=1
        elif(d[i]=='e' or d[i]=='E'):
            v[1]+=1
        elif(d[i]=='i' or d[i]=='I'):
            v[2]+=1
        elif(d[i]=='o' or d[i]=='O'):
            v[3]+=1
        elif(d[i]=='u' or d[i]=='U'):
            v[4]+=1
    return v

print("\n\nA quantidade de espaços em branco na frase é: "+str(count_space(s))+".")

print("\n\nA quantidade das seguintes vogais é: ")
aux='aeiou'
j=0
for i in count_vowel(s):
    print("\""+aux[j]+"\": "+str(i)+".")
    j+=1 
