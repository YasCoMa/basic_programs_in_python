# -*- coding: cp1252 -*-
import  unittest as u
from should_dsl import should, should_not

class Numero_fracionario(object):
    def __init__(self, numerador, denominador):
        if(type(numerador)==int and type(denominador)==int):
            if(denominador==0):
                raise TypeError("O denominador não pode ser zero!")
            self.numerador=numerador
            self.denominador=denominador
            mdc=self._get_mdc(numerador)
            if(mdc<0):
                mdc=mdc*(-1)
            self.numerador=numerador/mdc
            self.denominador=denominador/mdc
        else:
            raise TypeError("Use um número inteiro!")

    def get_numerador(self):
        return self.numerador
    def get_denominador(self):
        return self.denominador

    def set_numerador(self, numerador):
        if(type(numerador)==int ):
            mdc=self._get_mdc(numerador)
            self.numerador=numerador/float(mdc)
            self.denominador=self.denominador/float(mdc)
        else:
            raise TypeError("Use um número inteiro!")

    def set_denominador(self, denominador):
        if(type(denominador)==int):
            if(denominador==0):
                raise TypeError("O denominador não pode ser zero!")
            mdc=self._get_mdc(denominador)
            self.numerador=self.numerador/mdc
            self.denominador=denominador/mdc
        else:
            raise TypeError("Use um número inteiro!")

    def somar(self,onf):
        mmc=self._get_mmc(onf.get_denominador())
        m1=mmc/self.denominador
        m2=mmc/onf.get_denominador()
        d_novo=mmc
        n_novo=(m1*self.numerador)+(m2*onf.get_numerador())
        r=Numero_fracionario(n_novo,d_novo)
        return r

    def subtrair(self,onf):
        mmc=self._get_mmc(onf.get_denominador())
        m1=mmc/self.denominador
        m2=mmc/onf.get_denominador()
        d_novo=mmc
        n_novo=(m1*self.numerador)-(m2*onf.get_numerador())
        r=Numero_fracionario(n_novo,d_novo)
        return r

    def multiplicar(self, onf):
        n_novo=self.numerador*onf.get_numerador()
        d_novo=self.denominador*onf.get_denominador()
        r=Numero_fracionario(n_novo,d_novo)
        return r

    def dividir(self, onf):
        n_novo=self.numerador*onf.get_denominador()
        d_novo=self.denominador*onf.get_numerador()
        r=Numero_fracionario(n_novo,d_novo)
        return r

    def representa_com_travessao(self):
        if(self.numerador<0 and self.denominador<0):
            self.numerador=self.numerador*(-1)
            self.denominador=self.denominador*(-1)
            
        a='%i'%(self.numerador)
        b='%i'%(self.denominador)

        return a+'/'+b

    def representa_com_ponto(self,q_decimais):
        k='%i'%(q_decimais)
        formatter="%."+k+"f"
        div=formatter%(self.numerador/float(self.denominador))

        return div

    def _get_mdc(self, sec):
        if(type(sec)!=dict and type(sec)!=list and type(sec)!=str and type(sec)!=set):
            if(self.denominador>sec):
                resto=self.denominador%sec
                aux=sec
            else :
                resto=sec%self.denominador
                aux=self.denominador

            div=0
            if(resto==0):
                div=aux
            a=1
            while (resto!=0):
                div=resto
                if(a==1):
                    resto=aux%resto
                else:
                    resto=div%resto
                    a=a+1
            return div

    def _get_mmc(self, valor):
        if(type(valor)!=dict and type(valor)!=list and type(valor)!=str and type(valor)!=set):
            mdc=self._get_mdc(valor)
            mmc=(self.denominador*valor)/mdc
            return mmc
        else:
            raise TypeError("Parâmetro não é um número!")

class TestNumero_fracionario(u.TestCase):
    def test_inicializacao(self):
        q=Numero_fracionario(2,8)
        q.numerador | should | equal_to(1)
        q.denominador | should | equal_to(4)

    def test_representaComTraco(self):
        q=Numero_fracionario(-4,6)
        q.representa_com_travessao() | should | equal_to("-2/3")

    def test_representaComPonto(self):
        q=Numero_fracionario(-3,4)
        q.representa_com_ponto(3) | should | equal_to("-0.750")

    def test_soma(self):
        q=Numero_fracionario(2,6)
        w=Numero_fracionario(1,3)
        q.somar(w).get_numerador() | should | equal_to(2)
        q.somar(w).get_denominador() | should | equal_to(3)

    def test_subtracao(self):
        q=Numero_fracionario(4,5)
        w=Numero_fracionario(6,10)
        q.subtrair(w).get_numerador() | should | equal_to(1)
        q.subtrair(w).get_denominador() | should | equal_to(5)

    def test_multiplicacao(self):
        q=Numero_fracionario(1,2)
        w=Numero_fracionario(3,5)
        q.multiplicar(w).get_numerador() | should | equal_to(3)
        q.multiplicar(w).get_denominador() | should | equal_to(10)

    def test_divisao(self):
        q=Numero_fracionario(2,1)
        w=Numero_fracionario(1,2)
        q.dividir(w).get_numerador() | should | equal_to(4)
        q.dividir(w).get_denominador() | should | equal_to(1)
    
    def test_validationParameters(self):
        (Numero_fracionario, "a",1) | should | throw(TypeError, message="Use um número inteiro!")
        (Numero_fracionario, [1,2],1) | should | throw(TypeError, message="Use um número inteiro!")
        (Numero_fracionario, 1,{1,2}) | should | throw(TypeError, message="Use um número inteiro!")

        q=Numero_fracionario(2,8)
        (q.set_numerador, "a") | should | throw(TypeError, message="Use um número inteiro!")
        (q.set_numerador, [1,2]) | should | throw(TypeError, message="Use um número inteiro!")
        (q.set_numerador, {1,2}) | should | throw(TypeError, message="Use um número inteiro!")

        (q.set_denominador, "a") | should | throw(TypeError, message="Use um número inteiro!")
        (q.set_denominador, [1,2]) | should | throw(TypeError, message="Use um número inteiro!")
        (q.set_denominador, {1,2}) | should | throw(TypeError, message="Use um número inteiro!")

        (Numero_fracionario, 3,0) | should | throw(TypeError, message="O denominador não pode ser zero!")
        (q.set_denominador, 0) | should | throw(TypeError, message="O denominador não pode ser zero!")

if(__name__=='__main__'):
    u.main()
