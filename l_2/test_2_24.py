import  unittest as u
from should_dsl import should, should_not

class Retangulo(object):
    def __init__(self, base, altura):
        if (base <= 0 or altura<=0):
            raise ValueError
        self.base=base
        self.altura=altura

    def set_lados(self, base, altura):
        if (base <= 0 or altura<=0):
            raise ValueError
        self.base=base
        self.altura=altura

    def get_lados(self):
        return self.base, self.altura

    def get_area(self):
        return self.base*self.altura

    def get_perimetro(self):
        return (self.base*2)+(self.altura*2)

class TestRetangulo(u.TestCase):
        def test_inicializacao(self):
            q=Retangulo(5,10)
            q.base | should | equal_to(5)
            q.altura | should | equal_to(10)

        def test_alterarValores(self):
            q=Retangulo(5,10)
            q.set_lados(12,32)
            q.base | should | equal_to(12)
            q.altura | should | equal_to(32)

        def test_consultarValores(self):
            q=Retangulo(5,10)
            q.set_lados(12,32)
            q.get_lados() | should | equal_to((12,32))

        def test_getArea(self):
            q=Retangulo(5,10)
            q.get_area() | should | equal_to(50)

        def test_getPerimetro(self):
            q=Retangulo(5,10)
            q.get_perimetro() | should | equal_to(30)

        def test_validaAlterarLado(self):
            q=Retangulo(5,10)
            (q.set_lados , -1,3) | should | throw(ValueError)
            (q.set_lados , 0,3) | should | throw(ValueError)

if(__name__=='__main__'):
    u.main()
