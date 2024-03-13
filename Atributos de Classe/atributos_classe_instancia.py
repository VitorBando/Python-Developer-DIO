class Estudante:
    escola = 'DIO'

    def __init__(self, nome, numero) -> None:
        self.nome = nome
        self.numero = numero

    def __str__(self) -> str:
        return f"{self.nome} - {self.numero} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante('Guilherme', 1)
aluno_2 = Estudante('Vitor', 2)

mostrar_valores(aluno_1, aluno_2)

Estudante.nome = 'Python'

aluno_3 = Estudante('Chappie', 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
