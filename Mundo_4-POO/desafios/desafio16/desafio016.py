#Crie a classe funcionário, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita esse funcionário
# se apresentar

from rich import print
# Declaração da classe
class Funcionario:
    """
    Colhe os dados de um funcionário e o apresenta
    """
    # Atributos de classe
    empresa = "Curso em Video"
    def __init__(self,nome,cargo, setor): # Método construtor
        # Attributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self):
        print (f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa}")


# Declaração dos objetos

p1 = Funcionario("Matheus", "Programador", "TI")

p1.apresentação()

