# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."




# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Matheus"
g1.idade = 28
g1.aniversario()

print(g1.mensagem())