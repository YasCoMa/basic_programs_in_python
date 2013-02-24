from should_dsl import should
import unittest as u

class Bola (object):
    def __init__(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color=color

class Teste_bola(u.TestCase):
    # o nome do teste deve obrigatoriamente come�ar com "test"
    def test_possui_cor(self):
        b = Bola('Azul')
        b.get_color() |should| equal_to('Azul')
        
    def test_modifica_cor(self):
        b = Bola('Azul')
        b.set_color('Azul turquesa')
        b.get_color() |should| equal_to('Azul turquesa')
        
if __name__=="__main__":
    u.main()
    # Teste simples
    #print('Programa em execução...')
    #bola = Bola("Azul")

    #if(bola.get_color()=="Azul"):
        #print('Passou no teste 1.')

    #bola.set_color(input("Digite a nova cor da bola: "))
    #bola.set_color("Azul turquesa")
    #if(bola.get_color()=="Azul turquesa"):
        #print('Passou no teste 2.')
    #print(bola.get_color())

    # Teste automatizado
