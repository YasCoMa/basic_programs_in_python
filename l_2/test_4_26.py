# -*- coding: cp1252 -*-
import  unittest as u
from should_dsl import should, should_not

class Televisao (object):
    def __init__(self):
        self.on=False
        self.channel=0
        self.volume=0
        
    def ligar(self):
        self.on=True
        self.channel=1
        self.volume=50

    def desligar(self):
        self.on=False

    def get_canal(self):
        if(not self.on):
            raise TypeError("A televisão está desligada!")
        return self.channel

    def get_volume(self):
        if(not self.on):
            raise TypeError("A televisão está desligada!")
        return self.volume
    
    def troca_canal(self, channel):
        if(not self.on):
            raise TypeError("A televisão está desligada!")
        if(channel<1 or channel>60):
            raise TypeError("Canal fora da faixa, 1 a 60.")
        self.channel=channel
        
    def troca_volume(self, volume):
        if(not self.on):
            raise TypeError("A televisão está desligada!")
        if(volume<0 or volume>100):
            raise TypeError("Volume fora da faixa, 0 a 100.")
        self.volume=volume
        
class TestTelevisao(u.TestCase):
    def test_inicializacao(self):
        q=Televisao()
        q.on | should | equal_to(False)
        q.channel | should | equal_to(0)
        q.volume | should | equal_to(0)
        
    def test_ligar(self):
        q=Televisao()
        q.ligar()
        q.on | should | equal_to(True)

    def test_desligar(self):
        q=Televisao()
        q.desligar()
        q.on | should | equal_to(False)

    def test_getCanal(self):
        q=Televisao()
        q.ligar()
        q.get_canal() | should | equal_to(1)

    def test_getVolume(self):
        q=Televisao()
        q.ligar()
        q.get_volume() | should | equal_to(50)

    def test_trocaCanal(self):
        q=Televisao()
        q.ligar()
        q.troca_canal(5)
        q.get_canal() | should | equal_to(5)

    def test_trocaVolume(self):
        q=Televisao()
        q.ligar()
        q.troca_volume(70)
        q.get_volume() | should | equal_to(70)

    def test_validationForaDaFaixa(self):
        q=Televisao()
        q.ligar()
        (q.troca_canal, 80) |should| throw(TypeError, message="Canal fora da faixa, 1 a 60.")
        (q.troca_volume, 120) |should| throw(TypeError, message="Volume fora da faixa, 0 a 100.")

    def test_validationTvDesligada(self):
        q=Televisao()
        (q.get_canal) |should| throw(TypeError, message="A televisão está desligada!")
        (q.get_volume) |should| throw(TypeError, message="A televisão está desligada!")
        (q.troca_canal, 21) |should| throw(TypeError, message="A televisão está desligada!")
        (q.troca_volume, 45) |should| throw(TypeError, message="A televisão está desligada!")
        
if(__name__=='__main__'):
    u.main()
