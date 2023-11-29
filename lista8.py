#Crie quatro classes principais: Animal, Carnivoro, Herbivoro e Onivoro. A classe Animal será a classe
#base, enquanto as classes Carnivoro, Herbivoro e Onivoro serão classes intermediárias que
#herdarão da classe Animal e representarão diferentes tipos de dietas alimentares.
import random

class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def exibirDescrição(self):
        print('nome do animal: ',self.nome)
    
class Carnivoro(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def caçar(self):
        print(self.nome,'está caçando')
    
    def exibirDescrição(self):
        super().exibirDescrição()
        print('animal carnívoro')

class Herbivoro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def pastar(self):
        print(self.nome,'está pastando')
    
    def exibirDescrição(self):
        super().exibirDescrição()
        print('animal herbívoro')
    
class Onivoro(Carnivoro,Herbivoro):
    def __init__(self, nome):
        super().__init__(nome)
    
    def comer(self):
        num = random.randint(0,1)
        if num == 0:
            self.caçar()
        else:
            self.pastar()
    
    def exibirDescrição(self):
        super().exibirDescrição()
        print('animal onívoro')

leão = Carnivoro('Leão')
leão.exibireDescrição()
leão.caçar()

vaca = Herbivoro('Vaca')
vaca.exibirDescrição()
vaca.pastar()

cobra = Onivoro('Cobra')
cobra.exibirDescrição()
cobra.comer()
