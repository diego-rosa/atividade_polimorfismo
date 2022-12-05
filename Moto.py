from Automovel import Automovel

class Moto(Automovel):

    def __init__(self,marcaM,qtdRodasM,modeloM,velocidadeM,potenciaDoMotor,partidaEletrica):
        super().__init__(marcaM, qtdRodasM, modeloM, velocidadeM ,potenciaDoMotor)
        self.partidaEletrica = partidaEletrica

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Partida Elétrica: ",self.partidaEletrica)
