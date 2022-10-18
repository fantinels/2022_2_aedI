from Lista import Lista

l1 = Lista()

print('Antes de Ordenar')
l1.adicionar('Paola')
l1.adicionar('Ana')
l1.adicionar('Zimara')
l1.adicionar('Carlos')

print('Depois de Ordenar')
l1.adicionarOrdem()

print('Depois de Excluir')
l1.remover('Paola')