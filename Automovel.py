from Veiculo import Veiculo

class Automovel(Veiculo):

    def __init__(self,marcaA,qtdRodasA,modeloA,velocidadeA,potenciaDoMotor):
        super().__init__(marcaA,qtdRodasA,modeloA,velocidadeA)
        self.potenciaDoMotor = potenciaDoMotor


    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Potência do motor: " , self.potenciaDoMotor)
