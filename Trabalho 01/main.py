from Desktop import Desktop
from Notebook import Notebook

print("----- DESKTOP -----")
desk = Desktop()
desk.cadastrar('aa', 'preto', 1600, '10w')
print(desk.getInformacoes())

print("----- NOTEBOOK -----")
note = Notebook()
note.cadastrar('bb', 'cinza', 2000, '5 horas')
print(note.getInformacoes())