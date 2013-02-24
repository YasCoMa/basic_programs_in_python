# -*- coding: cp1252 -*-
import  unittest as u
from should_dsl import should, should_not

class Carnivoro(object):
    def __init__(self):
        self.alimentos=[]

    def alimentar(self, food):
        self.alimentos.append(food)

    def digerir(self):
        if(self.alimentos==[]):
            raise TypeError("Não há nada a digerir!")
        self.alimentos.remove(self.alimentos[0])

    def get_alimentos(self):
        return self.alimentos

class TestCarnivoro(u.TestCase):
    def test_inicializacao(self):
        q=Carnivoro()
        q.alimentos | should | equal_to([])

    def test_getAlimentos(self):
        q=Carnivoro()
        q.get_alimentos() | should | equal_to([])

    def test_alimentar(self):
        q=Carnivoro()
        q.alimentar(3)
        q.alimentar("Sam")
        q.alimentar([3,90,"&"])
        q.get_alimentos() | should | equal_to([3,"Sam",[3,90,"&"]])

    def test_digerir(self):
        q=Carnivoro()
        q.alimentar(4)
        q.alimentar("Dumper")
        q.alimentar([4,"*",{"a":1,"b":2}])
        q.digerir()
        q.get_alimentos() | should | equal_to(["Dumper",[4,"*",{"a":1,"b":2}]])

    def test_validationParameters(self):
        q=Carnivoro()
        (q.digerir) | should | throw(TypeError, message="Não há nada a digerir!")

if(__name__=='__main__'):
    u.main()
