import random as r
import time as t

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*- Corrida entre a lebre e a tartaruga -*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Bang...")
print("E eles partiram!")
timeline=[]
for i in range(70):
    if(i==0):
        timeline.append("[1: Ouch!!!]")
    timeline.append("[ ]")
    print(timeline[i],end="")

print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

pos_t=0
pos_l=0

sit_t=""
sit_l=""

while(pos_t!=69 and pos_l!=69):
    n=int(r.random()*10)
    if(n>=1 and n<=5):
        timeline[pos_t]='[ ]'
        pos_t+=3
        sit_t="Fez um movimento rápido..."
    elif(n>=6 and n<=7):
        timeline[pos_t]='[ ]'
        if(pos_t-6>=0):
            pos_t-=6
        else:
            pos_t=0
        sit_t="Levou um escorregão..."
    elif(n>=8 and n<=10):
        timeline[pos_t]='[ ]'
        pos_t+=1
        sit_t="Fez um movimento lento..."
               
    n=int(r.random()*10)
    if(n>=1 and n<=2):
        timeline[pos_l]='[ ]'
        pos_l*=1
        sit_l="Tirou uma soneca...."
    elif(n>=3 and n<=4):
        timeline[pos_l]='[ ]'
        if(pos_l-12>=0):
            pos_l-=12
        else:
            pos_l=0
        sit_l="Levou um grande escorregão..."
    elif(n>=5 and n<=6):
         timeline[pos_l]='[ ]'
         pos_l+=9
         sit_l="Deu um salto grande..."
    elif(n>=7 and n<=8):
         timeline[pos_l]='[ ]'
         pos_l+=1
         sit_l="Deu um salto pequeno..."
    elif(n>=9 and n<=10):
        timeline[pos_l]='[ ]'
        if(pos_l-2>=0):
            pos_l-=2
        else:
            pos_l=0
        sit_l="Levou um pequeno escorregão..."
        
    if(pos_t>=69 and pos_l<69):
        pos_t=69
        timeline[pos_t]="[T]"
        for k in range(70):
            print(timeline[k],end="")
        print("\n    Situação da tartaruga: "+sit_t)
        print("\n    Situação da lebre: "+sit_l)
        print("\n++++++++++++++++++++++++++ Tartaruga venceu!!! Yay!!! +++++++++++++++++++++++++\n")
        break
        
    elif(pos_l>=69 and pos_t<69):
        pos_l=69
        timeline[pos_t]="[T]"
        timeline[pos_l]="[L]"
        for k in range(70):
            print(timeline[k],end="")
        print("\n    Situação da tartaruga: "+sit_t)
        print("\n    Situação da lebre: "+sit_l)
        print("\n+++++++++++++++++++++++++++ Lebre venceu!!! Yuch!!! +++++++++++++++++++++++++\n")
        break
    
    elif(pos_t>=69 and pos_l>=69):
        timeline[69]="[Ouch!!!]"
        for k in range(70):
            print(timeline[k],end="")
        print("\n    Situação da tartaruga: "+sit_t)
        print("\n    Situação da lebre: "+sit_l)
        print("\n+++++++++++++++++++++++++++ Houve um empate +++++++++++++++++++++++++\n")
        break
    else:
        if(pos_t==pos_l):
            timeline[pos_t]='[Ouch!!!]'
        else:
            timeline[pos_t]="[T]"
            timeline[pos_l]="[L]"
        for k in range(70):
            print(timeline[k],end="")
        print("\n    Situação da tartaruga: "+sit_t)
        print("\n    Situação da lebre: "+sit_l)
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    
    t.sleep(2)
    
