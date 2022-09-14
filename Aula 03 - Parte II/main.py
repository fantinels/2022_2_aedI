from Cidade import Cidade
from Endereco import Endereco
from Pessoa import Pessoa


c1 = Cidade("Porto Alegre", "RS")
e1 = Endereco("Rua Coronel Genuíno, 130", c1)
# p1 = Pessoa("Paola Fantinel", "(51) 98357-3642", e1)

e1.imprimir()