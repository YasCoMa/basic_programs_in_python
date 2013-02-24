# -*- coding: cp1252 -*-
import  unittest as u
from should_dsl import should, should_not

class Numero(object):
    def __init__(self, valor):
        if(type(valor)!=dict and type(valor)!=list and type(valor)!=str and type(valor)!=set):
            self.value=valor
        else:
            raise TypeError("Parâmetro não é um número!")

    def get_valor(self):
        return self.value
    
    def set_valor(self, valor):
        if(type(valor)!=dict and type(valor)!=list and type(valor)!=str and type(valor)!=set):
            self.value=valor
        else:
            raise TypeError("Parâmetro não é um número!")

    def get_fatoresPrimos(self):
        fatores=[]
        f=2
        while(self.value%f!=0):
            f=f+1
        res=self.value/f
        fatores.append(f)
        while (res!=1):
            while (res%f==0):
                fatores.append(f)
                res=res/f
            f=f+1
            
        return fatores

    def get_fatorial(self):
        if(self.value<0):
            raise TypeError("Não existe fatorial de número negativo!")
        elif (self.value==0):
            f=1
        else:
            f=1
            for i in range(self.value):
                f=f*(i+1)
        return f

    def get_mdc(self, sec):
        if(type(sec)!=dict and type(sec)!=list and type(sec)!=str and type(sec)!=set):
            if (self.value==sec):
                raise TypeError("Números iguais, digite números diferentes")
            else:
                if(self.value>sec):
                    resto=self.value%sec
                    aux=sec
                else :
                    resto=sec%self.value
                    aux=self.value
                div=0
                a=1
                while (resto!=0):
                    div=resto
                    if(a==1):
                        resto=aux%resto
                    else:
                        resto=div%resto
                        a=a+1
                return div
        else:
            raise TypeError("Parâmetro não é um número!")

    def get_mmc(self, valor):
        if(type(valor)!=dict and type(valor)!=list and type(valor)!=str and type(valor)!=set):
            if (self.value==valor):
                raise TypeError("Números iguais, digite números diferentes")
            else:
                mdc=self.get_mdc(valor)
                mmc=(self.value*valor)/mdc
                return mmc
        else:
            raise TypeError("Parâmetro não é um número!")
        
class TestNumero(u.TestCase):
    def test_inicializacao(self):
        q=Numero(3)
        q.value | should | equal_to(3)
        q=Numero(-8)
        q.value | should | equal_to(-8)
        q=Numero(0)
        q.value | should | equal_to(0)

    def test_getEset(self):
        q=Numero(2)
        q.set_valor(5)
        q.get_valor() | should | equal_to(5)

    def test_getFatoresPrimos(self):
        q=Numero(60)
        q.get_fatoresPrimos() | should | equal_to([2,2,3,5])

    def test_getFatorial(self):
        q=Numero(5)
        q.get_fatorial() | should | equal_to(120)
        q.set_valor(0)
        q.get_fatorial() | should | equal_to(1)

    def test_getMDC(self):
        q=Numero(24)
        q.get_mdc(60) | should | equal_to(12)

    def test_getMMC(self):
        q=Numero(18)
        q.get_mmc(30) | should | equal_to(90)

    def test_validationParameters(self):
        (Numero, "a") | should | throw(TypeError, message="Parâmetro não é um número!")
        (Numero, [1,2]) | should | throw(TypeError, message="Parâmetro não é um número!")
        (Numero, {1,2}) | should | throw(TypeError, message="Parâmetro não é um número!")

        q=Numero(-3)
        (q.set_valor, "a") | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.set_valor, [1,2]) | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.set_valor, {1,2}) | should | throw(TypeError, message="Parâmetro não é um número!")

        (q.get_mdc, "a") | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.get_mdc, [1,2]) | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.get_mdc, {1,2}) | should | throw(TypeError, message="Parâmetro não é um número!")
        
        (q.get_mmc, "a") | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.get_mmc, [1,2]) | should | throw(TypeError, message="Parâmetro não é um número!")
        (q.get_mmc, {1,2}) | should | throw(TypeError, message="Parâmetro não é um número!")

        (q.get_fatorial) | should | throw(TypeError, message="Não existe fatorial de número negativo!")
        (q.get_mmc, -3) | should | throw(TypeError, message="Números iguais, digite números diferentes")
        (q.get_mdc, -3) | should | throw(TypeError, message="Números iguais, digite números diferentes")

if(__name__=='__main__'):
    u.main()
