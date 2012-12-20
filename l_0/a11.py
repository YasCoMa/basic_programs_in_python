s1 = input("Digite a primeira palavra: ")
s2 = input("Digite a segunda palavra: ")

def give_info_str(s1,s2):
    print("\nString 1: "+s1+".")
    print("\nString 2: "+s1+".")

    print("\n\nTamanho de \""+s1+ "\": "+str(len(s1))+" caracteres.")
    print("\nTamanho de \""+s2+ "\": "+str(len(s2))+" caracteres.")
    
    if (len(s1)!= len(s2)):
        print("\n\nAs strings são de tamanhos diferentes.")
        print("\n\nAs strins possuem conteúdos diferentes.")
    else:
        print("\n\nAs strings são de tamanhos iguais.")
        if(s1==s2):
            print("\n\nAs strins possuem conteúdos iguais.")
        else:
            print("\n\nAs strins possuem conteúdos diferentes.")

give_info_str(s1,s2)
