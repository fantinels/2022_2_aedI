from Moto import Moto
from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto

# v = Veiculo()
# v.imprimir()

c = Carro("BMW", 2022, 4)
c.imprimir()
print(f"Portas: {c.qtdPortas}")

m = Moto("Honda", 2010, True)
m.imprimir()
print(f"Partida: {m.partidaElet}")