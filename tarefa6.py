class Animal:
    def falar(self):
        print("O animal faz um som")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late")

class Gato(Animal):
    def falar(self):
        print("O gato mia")

animal1 = Animal()
animal2 = Cachorro()
animal3 = Gato()

animal1.falar()
animal2.falar()
animal3.falar()
