#1.Você foi contratado para desenvolver um programa de simulação de batalhas medievais. Para isso,
#você precisa implementar um sistema de unidades militares que possa se movimentar e atacar.
#Você deve criar três classes de unidades: Soldado, Arqueiro e Cavaleiro. Todas as classes devem
#herdar de uma classe base chamada UnidadeMilitar. A classe UnidadeMilitar deve ter os seguintes
#métodos:
unidades = []
class UnidadeMedieval:
    def __init__(self,nome):
        self.nome = nome

    def mover(self):
        print('movendo unidade de ',self.nome)
    
    def atacar(self):
        print('unidade de',self.nome,'atacando')
        
class Soldado(UnidadeMedieval):
    def __init__(self,nome):
        super().__init__(nome)

soldado = Soldado('Soldados')
unidades.append(soldado)

class Arqueiros(UnidadeMedieval):
    def __init__(self,nome):
        super().__init__(nome)

arqueiro = Arqueiros('Arqueiros')
unidades.append(arqueiro)

class Cavalheiro(UnidadeMedieval):
    def __init__(self,nome):
        super().__init__(nome)

cavalheiro = Cavalheiro('cavalheiros')
unidades.append(cavalheiro)

for i in range(len(unidades)):
    unidades[i].mover()
    unidades[i].atacar()

#2.Você está desenvolvendo um sistema para uma plataforma de streaming e precisa implementar a
#funcionalidade de assinaturas. Cada assinatura possui um tipo, um preço e detalhes específicos.
#assinaturas = []
class Assinatura():
    def __init__(self,tipo,preço,detalhes):
        self.tipo = tipo
        self.preço = preço
        self.detalhes = detalhes
    
    def calcular_preço(self):
        return self.preço
    
    def exibir_detalhes(self):
        return self.detalhes

class AssinaturaSimples(Assinatura):
    def __init__(self,tipo,preço,detalhes):
        super().__init__(tipo,preço,detalhes)

Simples = AssinaturaSimples('Assinatura Simples',29.99,'Assinatura básica que fornece acesso a filmes e séries em
qualidade padrão')
assinaturas.append(Simples)


class AssinaturaPremium(Assinatura):
    def __init__(self,tipo,preço,detalhes):
        super().__init__(tipo,preço,detalhes)

Premium = AssinaturaPremium('Assinatura Premium',49.99,'Assinatura avançada que oferece acesso a filmes e séries em
qualidade HD e Ultra HD')
assinaturas.append(Premium)


for i in (assinaturas):    
    print(Simples.tipo)
    a_simples_preço = Simples.calcular_preço()
    a_simples_detalhes = Simples.exibir_detalhes()
    print('preço = {}'.format(a_s_preço),'detalhes = ',a_simples_detalhes)
    print('')
    print(Premium.tipo)
    a_premium_preço = Premium.calcular_preço()
    a_premium_detalhes = Premium.exibir_detalhes()
    print('preço = {}'.format(a_p_preço),'detalhes = ',a_premium_detalhes)
    break
