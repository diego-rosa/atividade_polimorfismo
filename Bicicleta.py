from Veiculo import Veiculo

class Bicicleta(Veiculo):

    def __init__(self,marcaB,qtdRodasB,modeloB,velocidadeB,numMarchas,bagageiro):
        super().__init__(marcaB, qtdRodasB, modeloB, velocidadeB)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Número de Marchas: ",self.numMarchas)
        print("Bagageiro: ",self.bagageiro)
