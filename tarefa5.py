class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        if 0 <= nota <= 10:
            self.__nota = nota
        else:
            print("Nota inválida")

aluno1 = Aluno("João", 8)
print(aluno1.get_nota())

aluno1.set_nota(9)
print(aluno1.get_nota())
