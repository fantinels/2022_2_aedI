carro = {
    "modelo" : "Doblo",
    "ano" : 2006,
    "reboque" : False,
    "capacidade" : 950.243
}

print(carro)
print('-' * 20)

print('Ano: ', carro["ano"])
print('-' * 20)

print(carro.keys())
print('-' * 20)

print(carro.values())
print('-' * 20)

for chave, valor in carro.items():
    print(chave, ": ", valor)
print('-' * 20)

for chave in carro.keys():
    print(chave, ": ", carro[chave])
print('-' * 20)

print('----- TUPLA DE DICIONÁRIOS -----')

filho1 = {
    "nome" : "Júlia",
    "idade" : 14
}

filho2 = {
    "nome" : "Neymar",
    "idade" : 30
}

filho3 = {
    "nome" : "Maurício",
    "idade" : 22
}

filhos = (filho1, filho2)
filho1["nome"] = "Maurício"
filho1["email"] = "m@m.com"

del filho1["idade"]

print(filhos)