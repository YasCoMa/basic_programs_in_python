# -*- coding: cp1252 -*-
import  unittest as u
from should_dsl import should, should_not

class Numero_complexo(object):
    def __init__(self, real, imaginaria):
        if(type(real)!=dict and type(real)!=list and type(real)!=str and type(real)!=set and type(imaginaria)!=dict and type(imaginaria)!=list and type(imaginaria)!=str and type(imaginaria)!=set):
            self.real=real
            self.imaginaria=imaginaria
        else:
            raise TypeError("Parâmetro não é um número!")

    def get_real(self):
        return self.real
    def get_imaginaria(self):
        return self.imaginaria
    
    def set_real(self,real):
        if(type(real)!=dict and type(real)!=list and type(real)!=str and type(real)!=set):
            self.real=real
        else:
            raise TypeError("Parâmetro não é um número!")
        
    def set_imaginaria(self,imaginaria):
        if (type(imaginaria)!=dict and type(imaginaria)!=list and type(imaginaria)!=str and type(imaginaria)!=set):
            self.imaginaria=imaginaria
        else:
            raise TypeError("Parâmetro não é um número!")

    def representa(self, q_casasDecimais):
        k='%i'%(q_casasDecimais)
        formatter="%."+k+"f"
        a=formatter%(self.real)
        b=formatter%(self.imaginaria)
        
        if(self.imaginaria>=0):
            return a+'+'+b+'i' 
        else:
            return a+b+'i'
    
    def adicionar(self, onc):
        r_real=self.real+onc.get_real()
        r_imaginaria=self.imaginaria+onc.get_imaginaria()
        r=Numero_complexo(r_real,r_imaginaria)
        return r

    def subtrair (self, onc):
        r_real=self.real-onc.get_real()
        r_imaginaria=self.imaginaria-onc.get_imaginaria()
        r=Numero_complexo(r_real,r_imaginaria)
        return r

    def multiplicar(self, onc):
        r_real=(self.real*onc.get_real())-(self.imaginaria*onc.get_imaginaria())
        r_imaginaria=(self.imaginaria*onc.get_real())+(self.real*onc.get_imaginaria())
        r=Numero_complexo(r_real,r_imaginaria)
        return r

    def dividir(self, onc):
        div=(onc.get_real()*onc.get_real())+(onc.get_imaginaria()*onc.get_imaginaria())
        r_real=(self.real*onc.get_real())+(self.imaginaria*onc.get_imaginaria())/float(div)
        r_imaginaria=(self.imaginaria*onc.get_real())-(self.real*onc.get_imaginaria())/float(div)
        r=Numero_complexo(float(r_real),float(r_imaginaria))
        return r

class TesteNumero_complexo(u.TestCase):
    def test_inicializacao(self):
        q=Numero_complexo(3,8)
        q.real | should | equal_to(3)
        q.imaginaria | should | equal_to(8)

    def test_gettersAndSetters(self):
        q=Numero_complexo(3,8)
        q.set_real(-12)
        q.get_real() | should | equal_to(-12)
        q.set_imaginaria(24)
        q.get_imaginaria() | should | equal_to(24)

    def test_representa(self):
        q=Numero_complexo(3,-8)
        q.representa(2) | should | equal_to('3.00-8.00i')

    def test_adicionar(self):
        q=Numero_complexo(4,9)
        w=Numero_complexo(3,-8)
        q.adicionar(w).get_real()  | should | equal_to(7)
        q.adicionar(w).get_imaginaria() |  should | equal_to(1)
        
    def test_subtrair(self):
        q=Numero_complexo(4,9)
        w=Numero_complexo(3,-8)
        q.subtrair(w).get_real()  | should | equal_to(1)
        q.subtrair(w).get_imaginaria() |  should | equal_to(17)

    def test_multiplicar(self):
        q=Numero_complexo(5,1)
        w=Numero_complexo(2,-1)
        q.multiplicar(w).get_real()  | should | equal_to(11)
        q.multiplicar(w).get_imaginaria() |  should | equal_to(-3)

    def test_dividir(self):
        q=Numero_complexo(3,2)
        w=Numero_complexo(0,4)
        q.dividir(w).get_real()  | should | equal_to(0.5)
        q.dividir(w).get_imaginaria() |  should | equal_to(-0.75)

    def test_validationParameters(self):
        (Numero_complexo, "a", 1) | should | throw(TypeError, message="Parâmetro não é um número!")
        (Numero_complexo, [1,2], 1) | should | throw(TypeError, message="Parâmetro não é um número!")
        (Numero_complexo, {1,2}, 1) | should | throw(TypeError, message="Parâmetro não é um número!")

        q=Numero_complexo(1,1)
        (q.set_real, "a") | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.set_real, [1,2]) | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.set_real, {1,2}) | should | throw(TypeError, message="Parâmetro não é um número!")

        (q.set_imaginaria, "a") | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.set_imaginaria, [1,2]) | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.set_imaginaria, {1,2}) | should | throw(TypeError, message="Parâmetro não é um número!")
    
if(__name__=='__main__'):
    u.main()
