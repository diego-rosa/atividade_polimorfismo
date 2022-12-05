class Veiculo:

    def __init__(self,marca,qtdRodas,modelo,velocidade=0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirInformacoes(self):
        print("Marca: ",self.marca)
        print("qtdRodas: ",self.qtdRodas)
        print("Modelo: ",self.modelo)
        print("Velocidade Atual: ",self.velocidade)

    def acelerar(self,valor):
        x = self.velocidade + valor
        print("Velocidade após acelerar: ",x)

    def frear(self,valor):
        y = self.velocidade - valor
        if y > 0:
            print("Velocidade após frear: ",y)
        else:
            print("Velocidade após frear: Veiculo parado!")

    def espaco(self):
        print("---------------------")
        print()
