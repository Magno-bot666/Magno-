import random

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f"{self.valor} de {self.naipe}"


class Baralho:
    def __init__(self):
        self.cartas = self.criar_baralho()

    def criar_baralho(self):
        naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']
        baralho = [Carta(valor, naipe) for naipe in naipes for valor in valores]
        random.shuffle(baralho)
        return baralho

    def mostrar_cartas(self):
        for carta in self.cartas:
            print(carta)

    
    def bubble_sort(self, n=None):
        if n is None:
            n = len(self.cartas)

        if n == 1:
            return

        for i in range(n - 1):
            if self.cartas[i].valor > self.cartas[i + 1].valor:
                self.cartas[i], self.cartas[i + 1] = self.cartas[i + 1], self.cartas[i]
        
        
        self.bubble_sort(n - 1)

    
    def selection_sort(self, inicio=0):
        if inicio == len(self.cartas):
            return

        min_index = inicio
        for i in range(inicio + 1, len(self.cartas)):
            if self.cartas[i].valor < self.cartas[min_index].valor:
                min_index = i

        
        self.cartas[inicio], self.cartas[min_index] = self.cartas[min_index], self.cartas[inicio]

        
        self.selection_sort(inicio + 1)


if __name__ == '__main__':
    baralho = Baralho()
    
    print("Baralho embaralhado:")
    baralho.mostrar_cartas()
    
    print("\nOrdenando com Bubble Sort...")
    baralho.bubble_sort()
    baralho.mostrar_cartas()
    
    print("\nCriando um novo baralho e ordenando com Selection Sort...")
    baralho = Baralho()
    baralho.selection_sort()
    baralho.mostrar_cartas()
