from Fila import Fila

f1 = Fila()

f1.imprimir()
f1.adicionar('Paola')
f1.adicionar('João')
f1.adicionar('Maria')

f1.remover() # removeu Paola

f1.adicionar('Julia')

f1.remover() # removeu João
f1.remover() # removeu Maria
f1.remover() # removeu Julia