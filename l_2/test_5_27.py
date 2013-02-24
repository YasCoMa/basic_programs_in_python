# -*- coding: cp1252 -*-
import  unittest as u
from should_dsl import should, should_not

class Conta_corrente(object):
    def __init__(self, nome, numero):
        self.nome=nome
        self.numero=numero
        self.saldo=0

    def troca_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def get_numero(self):
        return self.numero

    def get_saldo(self):
        return self.saldo

    def faz_deposito(self, valor):
        self.saldo=self.saldo+valor

    def faz_saque(self, valor):
        if(valor>self.saldo):
            raise TypeError("O saldo é insuficiente!")
        self.saldo=self.saldo-valor

class TestContaCorrente(u.TestCase):
    def test_inicializacao(self):
        q=Conta_corrente("Highlander",5480)
        q.nome | should | equal_to("Highlander")
        q.numero | should | equal_to(5480)
        q.saldo | should | equal_to(0)
        
    def test_getters(self):
        q=Conta_corrente("Highlander",5480)
        q.get_nome() | should | equal_to("Highlander")
        q.get_numero() | should | equal_to(5480)
        q.get_saldo() | should | equal_to(0)
        
    def test_deposito(self):
        q=Conta_corrente("Highlander",5480)
        q.faz_deposito(4500)
        q.faz_deposito(50)
        q.get_saldo() | should | equal_to(4550)

    def test_saque(self):
        q=Conta_corrente("Highlander",5480)
        q.faz_deposito(500)
        q.faz_saque(50)
        q.get_saldo() | should | equal_to(450)

    def test_saqueSemSaldoSuficiente(self):
        q=Conta_corrente("Highlander",5480)
        (q.faz_saque, 50) | should | throw(TypeError, message="O saldo é insuficiente!")

if (__name__=='__main__'):
    u.main()
