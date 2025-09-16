from random import randint
class Pessoa:
    ano_atual= 2025
    lista = []

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascomento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def criar_id():
        while True:
            rand = randint(1000, 1999)
            if rand not in Pessoa.lista:
                Pessoa.lista.append(rand)
                return rand




p1= Pessoa.por_ano_nascimento('luiz', 1987)
#p1= Pessoa('Eduardo', 25)
p2= Pessoa('lucas', 20)
#print(f'nasceu no ano {p1.get_ano_nascomento()}',p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p1.nome, p1.idade)
print(p1.criar_id())
print()

#print(p1.get_ano_nascomento())
#print(p2.get_ano_nascomento())