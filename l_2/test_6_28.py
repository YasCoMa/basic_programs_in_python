# -*- coding: cp1252 -*-
import  unittest as u
from should_dsl import should, should_not

class Bomba_de_combustivel(object):
    def __init__(self, capacidade, preco_por_litro):
        if(capacidade<1 or preco_por_litro<1):
            raise ValueError
        self.capacidade=capacidade
        self.preco=preco_por_litro
        self.quant_atual=0

    def set_capacidade(self, capacidade):
        if(capacidade<1):
            raise ValueError
        self.capacidade=capacidade

    def set_preco(self,preco_por_litro):
        if(preco_por_litro<1):
            raise ValueError
        self.preco=preco_por_litro

    def set_quantAtual(self,quantidade):
        if(quantidade<1):
            raise ValueError
        self.quant_atual=quantidade
    
    def encher_bomba(self):
        self.quant_atual=self.capacidade

    def get_quantAtual(self):
        return self.quant_atual

    def get_capacidade(self):
        return self.capacidade

    def get_preco(self):
        return self.preco
    
    def abastecer_com_valor(self, valor):
        quant_a_abastecer=valor/self.preco
        if(self.quant_atual<quant_a_abastecer):
            raise TypeError("Quantidade insuficiente de combustível na bomba!")
        self.quant_atual=self.quant_atual-quant_a_abastecer
        return quant_a_abastecer

    def abastecer_com_litros(self,q_litros):
        if(self.quant_atual<q_litros):
            raise TypeError("Quantidade insuficiente de combustível na bomba!")
        self.quant_atual=self.quant_atual-q_litros
        return q_litros*self.preco
    
class TestBomba_de_combustivel(u.TestCase):
    def test_inicializacao(self):
        q=Bomba_de_combustivel(50,2.50)
        q.capacidade | should | equal_to(50)
        q.preco | should | equal_to(2.50)
        q.quant_atual | should | equal_to(0)

    def test_getters(self):
        q=Bomba_de_combustivel(50,2.50)
        q.get_capacidade() | should | equal_to(50)
        q.get_preco() | should | equal_to(2.50)
        q.get_quantAtual() | should | equal_to(0)

    def test_setters(self):
        q=Bomba_de_combustivel(50,2.50)
        q.set_capacidade(100)
        q.set_preco(1.50)
        q.set_quantAtual(30)
        q.get_capacidade() | should | equal_to(100)
        q.get_preco() | should | equal_to(1.50)
        q.get_quantAtual() | should | equal_to(30)

    def test_encherBomba(self):
        q=Bomba_de_combustivel(50,2.50)
        q.encher_bomba()
        q.get_quantAtual() | should | equal_to(50)

    def test_abasteceComValor(self):
        q=Bomba_de_combustivel(50,2.50)
        q.encher_bomba()
        q.abastecer_com_valor(25) | should | equal_to(10)
        q.quant_atual | should | equal_to(40)

    def test_abasteceComLitros(self):
        q=Bomba_de_combustivel(50,2.00)
        q.encher_bomba()
        q.abastecer_com_litros(24) | should | equal_to(48)
        q.quant_atual | should | equal_to(26)

    def test_validationNoCombustivel(self):
        q=Bomba_de_combustivel(50,2.00)
        (q.abastecer_com_litros, 24) | should | throw(TypeError, message="Quantidade insuficiente de combustível na bomba!")
        (q.abastecer_com_valor, 10) | should | throw(TypeError, message="Quantidade insuficiente de combustível na bomba!")
        
if(__name__=='__main__'):
    u.main()
