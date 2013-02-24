import  unittest
from should_dsl import should, should_not
#from a1 import Quadrado

class Quadrado(object) :
    def __init__(self, lado):
        if (lado <= 0):
            raise ValueError
        self.lado=lado

    def get_lado(self):
        return self.lado

    def alterar_lado(self, lado):
        if (lado <= 0):
            raise ValueError
        self.lado=lado   
        
    def get_area(self):
        return self.lado*self.lado

class TestQuadrado(unittest.TestCase) :
    def test_inicializacao(self):
        q=Quadrado(5)
        q.lado | should | equal_to(5)

    def test_getLado(self):
        q=Quadrado(5)
        q.get_lado() | should | equal_to(5)

    def test_alterarLado(self):
        q=Quadrado(5)
        q.alterar_lado(80)
        q.get_lado() | should | equal_to(80)
    
    def test_validaAlterarLado(self):
        q=Quadrado(5)
        (q.alterar_lado , -1) | should | throw(ValueError)
        (q.alterar_lado , 0) | should | throw(ValueError)

    def test_getArea(self):
        q=Quadrado(5)
        q.get_area() | should | equal_to(25)
        
if __name__ == '__main__':
    unittest.main()
