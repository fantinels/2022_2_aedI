jogadores = ('Maria', 'José', 'Júlia', 'Carlos', 'Joana', 'Marcelo')

print(jogadores)

print('-' * 20)

print(jogadores[2:-3])

print('-' * 20)

for pessoa in jogadores:
    print(pessoa)

print('-' * 20)

players = sorted(jogadores)
players[1] = 'Adalto'
print(players)

print('-' * 20)

def calcular(x, y):
    return (x + y), (x - y), (x * y), (x / y)

resultado = calcular(5, 10)

print(resultado)

print('-' * 20)