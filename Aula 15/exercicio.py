# num = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")

# usuario = int(input("Digite um número de 0 a 9: "))

# print(num[usuario])

nome = input("Digite seu nome: ")
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))

notas = {
    "nome" : nome,
    "nota1" : nota1,
    "nota2" : nota2
}

total = (nota1 + nota2) / 2

notas["total"] = total

print(notas)