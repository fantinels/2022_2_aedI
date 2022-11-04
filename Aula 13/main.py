from Fila import Fila

fifo = Fila()

fifo.add("ABC-1234", 240500)
fifo.add("BCD-2345", 5000)
fifo.add("DBC-1243", 1050)

fifo.remover()
fifo.remover()
fifo.add("FFF-1243", 150)
fifo.remover()
fifo.remover()