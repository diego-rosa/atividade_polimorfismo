from Veiculo import Veiculo
from Automovel import Automovel
from Carro import Carro
from Moto import Moto
from Bicicleta import Bicicleta

v1 = Veiculo("GM",4,"Gol",100)
v1.imprimirInformacoes()
v1.acelerar(100)
v1.frear(50)

v1.espaco()

a1 = Automovel("Chevrolet",4,"Voyage g5",60,1.6)
a1.imprimirInformacoes()
a1.acelerar(100)
a1.frear(50)

a1.espaco()

c1 = Carro("Fiat",4,"Palio",70,1.0,2)
c1.imprimirInformacoes()
c1.acelerar(100)
c1.frear(50)

c1.espaco()

m1 = Moto("Yamaha",2,"Factory",50,125,True)
m1.imprimirInformacoes()
m1.acelerar(100)
m1.frear(50)

m1.espaco()

b1 = Bicicleta("Monark",2,"off Road",10,25,True)
b1.imprimirInformacoes()
b1.acelerar(10)
b1.frear(5)
