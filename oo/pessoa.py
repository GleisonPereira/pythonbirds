class Pessoa:

    def __init__(self,nome=None,idade=25):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'olá'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Gleison'
    print(p.nome)
    print(p.idade)




