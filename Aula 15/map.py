def getTamanho(x):
    return len(x)

def aumentaPreco(p):
    return p * 1.1

frutas = ["Laranja", "Banana", "Abacaxi"]
jogadores = ('Maria', 'José', 'Júlia', 'Carlos', 'Joana', 'Marcelo')

tamFrutas = map(getTamanho, frutas)
print("Frutas: ", list(tamFrutas))

tamJog = map(getTamanho, jogadores)
print("Jogadores: ", list(tamJog))

precos = [6.00, 5.50, 4.99, 10.80]
print("Preços: ", precos)

novosPrecos = map(aumentaPreco, precos)
print("Novos Preços: ", list(novosPrecos))

print('-' * 20)

produto = {
    0 : 10.00,
    1 : 5.00,
    5 : 1.50
}

print(produto)

print('-' * 20)

novoProduto = map(aumentaPreco, produto.values())
print(list(novoProduto))