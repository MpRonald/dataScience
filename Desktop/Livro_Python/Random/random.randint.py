# -*- coding: utf-8 -*-
from random import randint

class Die():
    
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        
    def roll(self):
        return randint(1, num_sides)

"""
O método __init__() aceita um argumento opcional. Com essa classe, quando uma
instância de nosso dado for criada, o número de lados sempre será seis se 
nenhum argumento for incluído. Se um argumento for incluído, esse valor será 
usado para definir o número de lados do dado u. (Os dados são nomeados de 
acordo com o seu número de lados: um dado de seis lados é um D6, um dado de 
oito lados é um D8, e assim por diante.) O método roll() usa a função randint() 
para devolver um número aleatório entre 1 e o número de lados v. 
Essa função pode devolver o valor inicial (1), o valor final (num_sides) ou 
qualquer inteiro entre eles.
"""

dado1 = randint(1, 6)
print(f"Primeiro jogador = {dado1}")
dado2 = randint(1, 6)
print(f"Segundo jogador = {dado2}")

if dado1 > dado2:
    print("Primeiro jogador venceu!")
elif dado1 == dado2:
    print("Empate")
else:
    print("Segundo jogador venceu!")
    
    
#  exercicio 01    
frase = "esta é uma frase de exemplo"
print(len(frase.split()))

#  exercicio 02
i = 0
for j in range(1, 8):
    i = i + j
media = i / 7
print(media)


#  exercicio 03
nota1_aluno1 = float(input("Digite a primeira nota do aluno 1: "))
nota2_aluno1 = float(input("Digite a segunda nota do aluno 1: "))
print(30 * '=')
nota1_aluno2 = float(input("Digite a primeira nota do aluno 2: "))
nota2_aluno2 = float(input("Digite a segunda nota do aluno 2: "))
print(30 * '=')
nota1_aluno3 = float(input("Digite a primeira nota do aluno 3: "))
nota2_aluno3 = float(input("Digite a segunda nota do aluno 3: "))
print(30 * '=')
print("Médias dos alunos: \n")
print(f"Média aluno 1 : {(nota1_aluno1 + nota2_aluno1) / 2} ")
print(f"Média aluno 2 : {(nota1_aluno2 + nota2_aluno2) / 2} ")
print(f"Média aluno 3 : {(nota1_aluno3 + nota2_aluno3) / 2} ")

valores = []
contador = 1
for i in range(0, 7):
    valor = float(input(f"Digite o {contador}º valor: "))
    contador += 1
    valores.append(valor)
print(valores)
media = sum(valores) / 7
print(f"Média dos valores digitados: {round(media, 2)}")
    
    
print(valor)

valores = []

for i in range(7):
  valor = input()#recebendo valor
  valor = float()#convewrtendo valor recebido para float
  #armazenando valor na lista de valores
  valores.(valor)

#variável para armazenar soma de valores
soma = 0
#somando valores
for i in range(7):
  #adicionando cada valor da lista à soma total
  soma = valores + valores
  #imprimindo valores
  print(valores[i])

media = __

print('média:', ___)    
















