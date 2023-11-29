import math
#1.Hierarquia de Figuras Geométricas: considere as seguintes figuras geométricas: retângulo, triângulo
#e círculo. Crie uma hierarquia de classes para representar essas figuras geométricas. Cada classe
#deve ter os seguintes atributos:

class Figura_Geometrica:
    def __init__(self,nome,base,altura):
        self.nome = nome
        self.base = base
        self.altura = altura

class Retangulo(Figura_Geometrica):
    def __init__(self,nome,base,altura):
        super().__init__(nome,base,altura)
                

    def calcular_area(self):
        area = self.base * self.altura 
        return area

    def calcular_perimetro(self):
        perimetro = (self.altura*2)+(self.base*2)
        return perimetro

r1=Retangulo('retangulo',4,5)

perimetro_r = r1.calcular_perimetro()

area_r = r1.calcular_area()

print('perímetro do retângulo: ',perimetro_r,"\nÁrea do retângulo: ",area_r)

class Triangulo(Figura_Geometrica):
    def __init__(self, nome, base, altura):
        super().__init__(nome, base, altura)
        self.nome = 'Triângulo'

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area

    def calcular_perimetro(self):
        perimetro = self.base * 3
        return perimetro
t1 =Triangulo('triângulo',12,5)

perimetro_t = t1.calcular_perimetro()
area_t = t1.calcular_area()

print('Perímetro do triângulo: ',perimetro_t,'\nÁrea do triângulo: ',area_t)


class Circulo(Figura_Geometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        self.area = (2*math.pi)*(self.raio**2)
        return self.area

    def calcular_circunferência(self):
        circunferencia = (2*math.pi)*self.raio
        return circunferencia

c1 = Circulo(33)
c1_area = c1.calcular_area()
c1_circunferencia = c1.calcular_circunferencia()

print('Área do círculo: ',c1_area,'\nCircunferencia do círculo: ',c1_circunferencia)

#2.Crie uma classe base chamada Veiculo com os seguintes atributos:

class Veículo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def acelerar(self):
        print("Acelerando")

    
    def frear(self):
        print('Freando')


class Carro(Veículo):
    def __init__(self,cor,marca,modelo,ano):
        super().__init__(marca,modelo,ano)
        self.cor = cor

    def ligar_radio(self):
        print('Radio ligado')
    
    def abrir_porta(self):
        print('Abrindo porta')
Carro = Carro('vermelho','Ferrari','SF-23',2023)
Carro.acelerar()
Carro.ligar_radio()
Carro.frear()
Carro.abrir_porta()

class Moto(Veículo):
    def __init__(self,cilindrada,marca,modelo,ano):
        super().__init__(marca,modelo,ano)
        self.cilindrada = cilindrada
    
    def empinar(self):
        print('empinando')
    
    def buzinar(self):
        print('Buzinando')
    
class Caminhao(Veículo):
    def __init__(self,carga_maxima,marca,modelo,ano):
        super().__init__(marca,modelo,ano)
        self.carga_maxima = carga_maxima
    
    def carregar(self):
        print('carregando')
    
    def descarregar(self):
        print('descarregando')
    
#3.Desenvolva uma classe base chamada Criptografia que contenha os métodos cifrar e decifrar. Essa
#classe servirá como base para as subclasses CifraCesar e CifraXor, que implementarão algoritmos
#de criptografia específicos.

class Criptografia:
    def cifrar(self, texto):
        pass

    def decifrar(self, texto_cifrado):
        pass


class CifraCesar(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for letra in texto:
            if letra.isalpha():
                if letra.isupper():
                    codigo = ord(letra) - ord('A')
                    codigo = (codigo + self.chave) % 26
                    letra_cifrada = chr(codigo + ord('A'))
                else:
                    codigo = ord(letra) - ord('a')
                    codigo = (codigo + self.chave) % 26
                    letra_cifrada = chr(codigo + ord('a'))
                texto_cifrado += letra_cifrada
            else:
                texto_cifrado += letra
        return texto_cifrado

    def decifrar(self, cifrado):
        decifrado = ""
        for letra in cifrado:
            if letra.isalpha():
                if letra.isupper():
                    codigo = ord(letra) - ord('A')
                    codigo = (codigo - self.chave) % 26
                    letra_decifrada = chr(codigo + ord('A'))
                else:
                    codigo = ord(letra) - ord('a')
                    codigo = (codigo - self.chave) % 26
                    letra_decifrada = chr(codigo + ord('a'))
                decifrado += letra_decifrada
            else:
                decifrado += letra
        return decifrado


class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for letra in texto:
            letra_cifrada = chr(ord(letra) ^ self.chave)
            texto_cifrado += letra_cifrada
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)
    
texto = "Hello, World!"
chave_cesar = 3
chave_xor = 7

cifra_cesar = CifraCesar(chave_cesar)
texto_cifrado_cesar = cifra_cesar.cifrar(texto)
texto_decifrado_cesar = cifra_cesar.decifrar(texto_cifrado_cesar)

cifra_xor = CifraXor(chave_xor)
texto_cifrado_xor = cifra_xor.cifrar(texto)
texto_decifrado_xor = cifra_xor.decifrar(texto_cifrado_xor)

print("Cifra de César:")
print("Texto cifrado:", texto_cifrado_cesar)
print("Texto decifrado:", texto_decifrado_cesar)

print("\nAlgoritmo XOR:")
print("Texto cifrado:", texto_cifrado_xor)
print("Texto decifrado:", texto_decifrado_xor)
