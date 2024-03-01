class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor =cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Plim Plim...')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta Parada')

    def correr(self):
        print('Vrummmm...')

    def get_cor(self):
        return self.cor            

    # def __str__(self):
    #    return f'Bicicleta: Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: {self.valor}'

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta('vermelha','caloi',2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('verde', 'monark', 2000, 189)
b2.buzinar() # Bicileta.buzinar(b2)
print(b2.cor)