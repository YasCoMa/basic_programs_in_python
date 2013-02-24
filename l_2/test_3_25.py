import  unittest as u
from should_dsl import should, should_not

class Pessoa(object):
    def __init__(self, idade, peso, altura):
        self.idade=idade
        self.peso=peso
        self.altura=altura

    def get_dados(self):
        return self.idade, self.peso,self.altura

    def set_dados(self,idade,peso,altura):
        if (idade<0 or peso<0 or altura<0):
            raise ValueError
        self.idade=idade
        self.peso=peso
        self.altura=altura

    def get_idade(self):
        return self.idade
    def get_peso(self):
        return self.peso
    def get_altura(self):
        return self.altura

    def set_idade(self, idade):
        if(idade<0):
            raise ValueError
        self.idade=idade
    def set_peso(self, peso):
        if(peso<0):
            raise ValueError
        self.peso=peso
    def set_altura(self, altura):
        if(altura<=0):
            raise ValueError
        self.altura=altura

    def envelhece(self, q_anos):
        if(q_anos<0):
            raise ValueError
        if (self.idade<21):
            desconto=(self.idade+q_anos)-21
            if(desconto<=0):
                self.idade=self.idade+q_anos
                self.altura=self.altura+(q_anos*0.015)
            else:
                self.idade=self.idade+q_anos
                self.altura=self.altura+((q_anos-desconto)*0.015)
        else:
            self.idade=self.idade+q_anos
                
    def engorda(self, q_kg):
        if (q_kg<0):
            raise ValueError
        self.peso=self.peso+q_kg

    def emagrece(self, q_kg):
        if (q_kg<0 or (self.peso-q_kg)<0):
            raise ValueError
        self.peso=self.peso-q_kg

class TestPessoa(u.TestCase):
    def test_inicializacao(self):
        q=Pessoa(19,50,1.50)
        q.idade | should | equal_to(19)
        q.peso | should | equal_to(50)
        q.altura | should | equal_to(1.50)

    def test_generalGettersAndSetters(self):
        q=Pessoa(19,50,1.50)
        q.set_dados(21,67,2.1)
        q.get_dados()  | should | equal_to((21,67,2.1))

    def test_individualGettersAndSetters(self):
        q=Pessoa(19,50,1.50)
        q.set_idade(21)
        q.set_peso(67)
        q.set_altura(2.1)
        q.get_idade()  | should | equal_to(21)
        q.get_peso()  | should | equal_to(67)
        q.get_altura() | should | equal_to(2.1)

    def test_envelhece(self):
        q=Pessoa(19,50,1.50)
        q.envelhece(1)
        q.get_idade()  | should | equal_to(20)
        q.get_altura()  | should | equal_to(1.515)
        q.envelhece(2)
        q.get_idade()  | should | equal_to(22)
        q.get_altura()  | should | close_to(1.530, delta=0.0001)

    def test_engorda(self):
        q=Pessoa(19,50,1.50)
        q.engorda(3)
        q.get_peso() | should | equal_to(53)

    def test_emagrece(self):
        q=Pessoa(19,50,1.50)
        q.emagrece(8)
        q.get_peso() | should | equal_to(42)

    def test_validationParameters(self):
        q=Pessoa(19,50,1.50)
        (q.set_idade, -1) | should | throw(ValueError)
        (q.set_peso, -67) | should | throw(ValueError)
        (q.set_altura, -2.1) | should | throw(ValueError)
        (q.set_dados, 4, -4, 2.1) | should | throw(ValueError)
        (q.envelhece, -3) | should | throw(ValueError)
        (q.engorda, -4) | should | throw(ValueError)
        (q.emagrece, -5) | should | throw(ValueError)
        
if(__name__=='__main__'):
    u.main()
