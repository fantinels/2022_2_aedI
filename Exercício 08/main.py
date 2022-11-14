from Torre import Torre
from Apartamento import Apartamento
from FilaEspera import FilaEspera

torre = Torre()
torre.cadastrar(1, 'torre1', 'aaaa')
torre.imprimir()

ap1 = Apartamento()
ap1.cadastrar(1, 124, torre)
ap1.imprimirApe()

ap2 = Apartamento()
ap2.cadastrar(2, 346, torre)
ap2.imprimirApe()

# FILA DE ESPERA
fila = FilaEspera()
fila.adicionarApe(ap1)
fila.adicionarApe(ap2)
fila.imprimir()

fila.remover(10)
fila.remover(20)
ap1.imprimirApe()
ap2.imprimirApe()