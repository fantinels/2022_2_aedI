from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

print("----- PESSOA -----")

p1 = Pessoa(1, 'Paola', 'Rua A', 51999994444)
p1.imprimirNome()

print("-" * 30)

# Testando GET
# print(p1.getCodigo())
# print(p1.getNome())
# print(p1.getEndereco())
# print(p1.getTelefones())

# Testando SET
p1.setCodigo(2)
print("Código:", p1.getCodigo())
p1.setNome('Paula')
print("Nome:", p1.getNome())
p1.setEndereco('Rua B')
print("Endereço:", p1.getEndereco())
p1.setTelefones(51333337777)
print("Fones:", p1.getTelefones())

print("-" * 30)

print("----- PESSOA FÍSICA -----")
# IMC arredondado
pf1 = Fisica(3, 'Pedro', 'Rua C', 51888887777, 77788899966, 20, 55, 1.65)
pf1.imprimirCpf()

# Testando GET
print(pf1.getCpf())
# print(pf1.getIdade())

# Testando SET
print("-" * 30)
pf1.setCpf(22299944466)
print("CPF:", pf1.getCpf())
pf1.setIdade(25)
print("Idade:", pf1.getIdade())

print("-" * 30)

print("----- PESSOA JURÍDICA -----")
pj1 = Juridica(4, 'Shop LTDA', 'Rua D', 51333337777, '22.777.999/0001-77', '777.999.888.888', 41)
pj1.imprimirCnpj()

print("-" * 30)

# Testando GET
# print(pj1.getCnpj())
# print(pj1.getInscricaoEstad())
# print(pj1.getQtdFunc())

# Testando SET
pj1.setCnpj('77.666.999/0001-88')
print("CPF:", pj1.getCnpj())
pj1.setInscricaoEstad('999.555.777.111')
print("N° Insc. Estad.:", pj1.getInscricaoEstad())
pj1.setQtdFunc(60)
print("Qtde Funcionários:", pj1.getQtdFunc())