from Automovel import Automovel

class Carro(Automovel):

    def __init__(self,marcaC,qtdRodasC,modeloC,velocidadeC,potenciaDoMotor,qtdPortas):
        super().__init__(marcaC,qtdRodasC,modeloC,velocidadeC,potenciaDoMotor)
        self.qtdPortas = qtdPortas

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Qtd Portas: ",self.qtdPortas)
