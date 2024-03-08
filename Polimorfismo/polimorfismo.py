class Passaro:
    def voar(self):
        print('Voando')


class Pardal(Passaro):
    def voar(self):
        super().voar()


class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar.')


class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando...')


def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()

plano_voo(Pardal())

plano_voo(Avestruz())

plano_voo(Aviao())
