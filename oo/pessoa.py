class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    gilmar = Pessoa(nome='Gilmar')
    luciano = Pessoa(gilmar, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    for filho in luciano.filhos:
        print(f'filho:{filho.nome}')

    luciano.sobrenome = "Silva"
    del gilmar.idade
    print(luciano.__dict__)
    print(gilmar.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(gilmar.olhos)
    gilmar.olhos = 3
    print(gilmar.olhos)
    del gilmar.olhos
    print(gilmar.olhos)