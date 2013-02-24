# -*- coding: cp1252 -*-
import  unittest as u
from should_dsl import should, should_not

class Ponto(object):
    def __init__(self, x,y):
        self.x=x
        self.y=y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
class Retangulo(object):
    def __init__(self, altura, largura):
        if(altura<=0 or largura<=0):
            raise ValueError
        self.altura=altura
        self.base=largura
        self.ponto_central=Ponto(0,0)
        self.ponto_1Q=Ponto(+(self.base/2), +(self.altura/2))
        self.ponto_2Q=Ponto(+(self.base/2), -(self.altura/2))
        self.ponto_3Q=Ponto(-(self.base/2), -(self.altura/2))
        self.ponto_4Q=Ponto(-(self.base/2), +(self.altura/2))

    def set_altura(self, altura):
        if(altura<=0):
            raise ValueError
        self.altura=altura
    
    def set_largura(self, largura):
        if(largura<=0):
            raise ValueError
        self.base=largura
    
    def get_area(self):
        return self.altura*self.base
    def get_perimetro(self):
        return (self.altura*2)+(self.base*2)
    def ehQuadrado(self):
        if (self.altura==self.base) :
            ehQuad=True
        else:
            ehQuad=False
        return ehQuad
    
    def get_altura(self):
        return self.altura
    def get_largura(self):
        return self.base
    def get_pontoCentral(self):
        return self.ponto_central
    
    def get_pontosDosVertices(self):
        return self.ponto_1Q, self.ponto_2Q, self.ponto_3Q, self.ponto_4Q
    def get_ponto1oQuad(self):
        return self.ponto_1Q
    def get_ponto2oQuad(self):
        return self.ponto_2Q
    def get_ponto3oQuad(self):
        return self.ponto_3Q
    def get_ponto4oQuad(self):
        return self.ponto_4Q
    
    def troca_pontoCentral(self, x, y):
        self.ponto_central=Ponto(x,y)
        self.ponto_1Q=Ponto(self.ponto_central.get_x()+(self.base/2), self.ponto_central.get_y()+(self.altura/2))
        self.ponto_2Q=Ponto(self.ponto_central.get_x()+(self.base/2), self.ponto_central.get_y()-(self.altura/2))
        self.ponto_3Q=Ponto(self.ponto_central.get_x()-(self.base/2), self.ponto_central.get_y()-(self.altura/2))
        self.ponto_4Q=Ponto(self.ponto_central.get_x()-(self.base/2), self.ponto_central.get_y()+(self.altura/2))

class TestRetanguloJoinPonto(u.TestCase):
    def test_inicializacao(self):
        q=Retangulo(4,4)
        q.base | should | equal_to(4)
        q.altura | should | equal_to(4)
        q.ponto_central .get_x()| should | equal_to(0)
        q.ponto_central .get_y()| should | equal_to(0)
        q.ponto_1Q .get_x()| should | equal_to(2)
        q.ponto_1Q .get_y()| should | equal_to(2)
        q.ponto_2Q .get_x()| should | equal_to(2)
        q.ponto_2Q .get_y()| should | equal_to(-2)
        q.ponto_3Q .get_x()| should | equal_to(-2)
        q.ponto_3Q .get_y()| should | equal_to(-2)
        q.ponto_4Q .get_x()| should | equal_to(-2)
        q.ponto_4Q .get_y()| should | equal_to(2)

    def test_getters(self):
        q=Retangulo(6,2)
        q.get_largura() | should | equal_to(2)
        q.get_altura() | should | equal_to(6)
        q.get_pontoCentral().get_x()| should | equal_to(0)
        q.get_pontoCentral().get_y()| should | equal_to(0)
        q.get_ponto1oQuad() .get_x()| should | equal_to(1)
        q.get_ponto1oQuad().get_y()| should | equal_to(3)
        q.get_ponto2oQuad() .get_x()| should | equal_to(1)
        q.get_ponto2oQuad().get_y()| should | equal_to(-3)
        q.get_ponto3oQuad() .get_x()| should | equal_to(-1)
        q.get_ponto3oQuad().get_y()| should | equal_to(-3)
        q.get_ponto4oQuad().get_x()| should | equal_to(-1)
        q.get_ponto4oQuad().get_y()| should | equal_to(3)

    def test_setters(self):
        q=Retangulo(4,8)
        q.set_largura(12)
        q.set_altura(5)
        q.get_largura()| should | equal_to(12)
        q.get_altura() | should | equal_to(5)

    def test_trocaPontoCentral(self):
        q=Retangulo(12,24)
        q.troca_pontoCentral(10,20)
        q.get_pontoCentral().get_x()| should | equal_to(10)
        q.get_pontoCentral().get_y()| should | equal_to(20)
        q.get_ponto1oQuad() .get_x()| should | equal_to(22)
        q.get_ponto1oQuad().get_y()| should | equal_to(26)
        q.get_ponto2oQuad() .get_x()| should | equal_to(22)
        q.get_ponto2oQuad().get_y()| should | equal_to(14)
        q.get_ponto3oQuad() .get_x()| should | equal_to(-2)
        q.get_ponto3oQuad().get_y()| should | equal_to(14)
        q.get_ponto4oQuad().get_x()| should | equal_to(-2)
        q.get_ponto4oQuad().get_y()| should | equal_to(26)

    def test_getArea(self):
        q=Retangulo(8,14)
        q.get_area() | should | equal_to(112)
        
    def test_getPerimetro(self):
        q=Retangulo(8,14)
        q.get_perimetro() | should | equal_to(44)

    def test_ehQuadrado(self):
        q=Retangulo(6,8)
        q.ehQuadrado() | should | equal_to(False)
        q.set_largura(6)
        q.ehQuadrado() | should | equal_to(True)

    def test_validationParameters(self):
        (Retangulo, -2, 4) | should | throw(ValueError)
        (Retangulo, -2, 0) | should | throw(ValueError)
        q=Retangulo(2,4)
        (q.set_largura, -1) | should | throw(ValueError)
        (q.set_largura, 0) | should | throw(ValueError)
        (q.set_altura, -5) | should | throw(ValueError)
        (q.set_altura, 0) | should | throw(ValueError)
        
if(__name__=='__main__'):
    u.main()
