"""
- Construa um algoritmo para implementar a classe Retângulo que possui os atributos: altura se largura.
- A classe deve ter os seguintes métodos:
    - Método construtor
    - Método que calcula a área do retângulo ( altura * largura) e retorna o resultado
    - Método que imprime os valores dos atributos da classe. 
"""

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura 

    def calcular_area(self):
        calculo = self.altura * self.largura
        return calculo

    def imprime_resultado(self):
        print(f"A altura é de {self.altura} e a largura de {self.largura}\nO retângulo tem a área de: {self.calcular_area()}")

area = Retangulo(3, 7)
area.imprime_resultado()