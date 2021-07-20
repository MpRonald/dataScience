# -*- coding: utf-8 -*-
"""
Livro pandas;
Capítulo 5 - Combinado DataFrames
"""

import pandas as pd

# Criando DataFrames;

lojaA = pd.DataFrame({"loja": ["A", "A", "A"], "dia":["sex", "sab", "dom"],
                      "valor":[7500, 9500, 8200]})

lojaB = pd.DataFrame({"loja":["B", "B", "B"], "dia":["sex", "sab", "dom"],
                      "valor":[5100, 8250, 9900]})

lojaC = pd.DataFrame({"loja":["C", "C"], "dia":["sab", "dom"],
                      "valor":[7500, 11800]})

# Concatenando DataFrames;
lojasABC = pd.concat([lojaA, lojaB, lojaC], ignore_index=True)
print(lojasABC)

# =============================================================================
# Neste exemplo usamos o concat() para concatenar as tres variavies, mesmo
# a lojaC tendo apenas duas linhas, este método é muito comum. 
# Usamos tbm o ignore_index=True, que força a geração de novos indices, caso
# isso não seja feito o Pandas usa as linhas originais dos dataFrames
# =============================================================================

# =============================================================================
# A concatenação faz sentido quando os DF tem a mesma origem e a mesa definição,
# ou seja contém os mesmo atributos
# =============================================================================

#Porém, nada impede de concatenarmos DF diferentes;
# Abaixo concatenamos DF diferentes;

import pandas as pd

d1 = pd.DataFrame({"carro":["Hyundai", "Reanult", "Fiat"]})
d2 = pd.DataFrame({"animal":["Capivara", "Bem-te-vi"]})

# Concatenando os DF;
d3 = pd.concat([d1,d2],ignore_index=True,sort=False)

# =============================================================================
# Teremos como resultado o NaN para que o DF seja alinhado, usamo o parametro
# sort=False para que o DF nao tente reordenar os atributos.
# =============================================================================

# União, interseção e diferença;
# =============================================================================
# => união -> concat() + drop_duplicates()
# => interseção -> merge()
# => diferença -> isin() + indexação booleana
# =============================================================================

# operações de conjunto;
import pandas as pd

df_sql = pd.DataFrame({"email":["rakesh@xyz.com", "ecg@acmecorpus.com"]})
df_python = pd.DataFrame({"email":["ana@xyz.com","jonas@acmecorpus.com",
                                   "rakesh@xyz.com"]})

# 1 -> efetua as operações de conjunto;
# 1.1 -> União(relação de alunos distintos)

alunos = pd.concat([df_sql, df_python], ignore_index=True)
alunos.drop_duplicates()

# 1.2 -> interseção(quem faz ambos os cursos)
sql_e_python = df_sql.merge(df_python)

# 1.3 -> diferença (quem fez só sql e quem fez só python)
so_sql = df_sql[df_sql.email.isin(df_python.email)==False]
so_python = df_python[df_python.email.isin(df_sql.email)==False]

print('------------------------------')
print('Alunos Distintos:')
print(alunos)
print('------------------------------')
print('Alunos cursaram SQL e Python:')
print(sql_e_python)
print('------------------------------')
print('Alunos cursaram apenas SQL:')
print(so_sql)
print('------------------------------')
print('Alunos cursaram apenas Python:')
print(so_python)

# =============================================================================
# Neste programa acima, foram criados dois DF, ao qual foram submetidos à 
# operações de conjunto na segunda parte do programa;
# Para realizar a opração união 1.1, utilizamos o concat(), seguido do
# método drop_duplicates() que como o nome sugere, remove as linhas duplicadas.
# Como sabemos o concat() serve para concatenar DFs.
# =============================================================================

# =============================================================================
# Para realizar a operação de interseção, parte 1.2, utilizamos o método
# merge(), que trata-se de fazer junção de DFs, porém quando usado sem nenhum
# parametro em uma operação que envolva DFs compátiveis, o resultado consiste 
# na interseção dos conjuntos;
# =============================================================================

# =============================================================================
# Por fim, falando da operação diferença, a diferença dos conjuntos "r" e "s"
# tem por objetivo determinar os elementos de r que não fazem parte de "s",
# no pd é preciso usar o método isin() em conjunto com a indexação booleana
# para que seja possível realizar esta operação.
# =============================================================================

# Comparando dois DFs;
# Para podermos comparar dois DFs podemos utilizar o método equals();

# comparação de DFs;
filmes1 = pd.DataFrame({"titulo":["O filho da Noiva", "La la land"],
                        "ano":[2001, 2017]})
filmes2 = pd.DataFrame({"titulo":["Noel poeta da vila", "La la land"],
                        "ano":[2007, 2017]})
filmes3 = pd.DataFrame({"titulo":["O filho da noiva", "La la land"],
                        "ano":[2001, 2017]})

# Verificando quais DFs são iguais;
print(f"Filme1 é igual à filme2 -> {filmes1.equals(filmes2)}")
print(f"Filme1 é igual à filme3 -> {filmes1.equals(filmes3)}")

# operação de junção;
# junção natural;
# =============================================================================
# A operação de junção Natural realiza o 'casamento (match)' de linhas de um
# DF "r" com linhas de num DF "s", no entanto a combinação é feita de forma
# seletiva, ou seja, combina apenas linhas que coincidem em quaiquer atributos
# que são comuns a ambos os DFs.
# =============================================================================

# =============================================================================
# O método merge() em Python/Pandas é utilizado para implementar todos os tipos
# de operação de junção. 
# =============================================================================

# Junção Natural;
import pandas as pd

# criando os DFs R e S;
R = pd.DataFrame({"a":[1,7], "b":[2,4]})
S = pd.DataFrame({"b":[2,4,9], "c":[3,6,1], "d":[5,9,5]})

# efetuando a operação de junção;
juncao_natural = pd.merge(R, S,on="b")
print(15*"-")
print(f"R: \n{R}")
print(15*"-")
print(f"S: \n{S}")
print(15*"-")
print(f"Junção Natural de R e S: \n{juncao_natural}")

# =============================================================================
# Conforme mostrado no programa, a sintaxe do método merge() para realizar 
# a junção interna de R e S é trivial. Basta especificar um par de DataFrames 
# como parâmetros, que o método merge() se encarrega de identificar, sozinho, 
# qual é o atributo comum a ambos e, assim, processar a junção.
# =============================================================================

# =============================================================================
# É possível indicar explicitamente qual é o atributo de ligação, bastando
# para isso utilizar o parametro on
# =============================================================================

pd.merge(R, S,on="b")

# =============================================================================
# Na junção natural, para um atributo ser considerado comum a R e S, ele 
# precisa ter o mesmo nome nestes dois DataFrames. No entanto, isso nem 
# sempre acontece quando estamos lidando com bases de dados reais. Na figura 
# a seguir, um exemplo que ilustra esse tipo situação é apresentado. Temos 
# dois DataFrames chamados depto (departamento) e emp (empregados), que 
# possuem o id do departamento como atributo de ligação. No entanto, este 
# atributo de ligação possui o nome diferente em cada DataFrame. Veja que 
# ele se chama id em depto e idDepto no DataFrame emp.
# =============================================================================

# Junção Interna
# =============================================================================
# Na junção interna, você deve indicar explicitamente a condição de junção
# para o método merge(). Isso significa especificar quais são os atributos 
# de ligação de cada DataFrame, utilizando para tal os parâmetros left_on e 
# right_on. A seguir, o uso destes parâmetros é demonstrado em um programa 
# que implementa a junção interna com o objetivo de combinar os dados dos 
# funcionários e com os dados de seus departamentos.
# =============================================================================

import pandas as pd

# Criando DataFrames;
dic_depto = {"id":["D1","D2","D3","D4"],
             "nomDepto": ["Compras","RH","TI","Vendas"],
             "local":["SP","RJ","RJ","SP"]}
dic_emp = {"num":[3199,3269,3555,3788,3844],
           "nome": ["Ana","David","José","Marina","Luís"],
           "salario":[1600,2975,1500,5000,3000],
           "idDepto": ["D2","D3",None,"D2","D4"]}

depto = pd.DataFrame(dic_depto)
emp = pd.DataFrame(dic_emp)

juncao_interna = pd.merge(emp, depto, left_on="idDepto", right_on="id")
print(20*"-")
print(f"Depto: \n{depto}")
print(20*"-")
print(f"emp: \n{emp}")
print(20*"-")
print(f"Junção Interna: \n{juncao_interna}")

# =============================================================================
# Conceitualmente, a junção interna funciona da mesma forma que a junção 
# natural, ou seja, ela combina uma linha de um DataFrame R com uma linha 
# de um DataFrame S apenas quando há coincidência nos valores das colunas 
# especificadas na condição de junção.
# =============================================================================

# =============================================================================
# Conceitualmente, a junção interna funciona da mesma forma que a junção 
# natural, ou seja, ela combina uma linha de um DataFrame R com uma linha 
# de um DataFrame S apenas quando há coincidência nos valores das colunas 
# especificadas na condição de junção. Para realizar a junção interna entre 
# dois DataFrames, basta seguir sempre a mesma receita: Especificar os nomes 
# dos DataFrames envolvidos na junção separados por vírgula, dentro do 
# método merge() (por exemplo, depto,emp). Utilizar o parâmetro left_on 
# indicando o nome do atributo de ligação no DataFrame que foi especificado 
# à esquerda (em nosso exemplo, emp foi especificado antes de depto, logo emp 
# é considerado o DataFrame à esquerda). Utilizar o parâmetro 
# right_on indicando o nome do atributo de ligação no DataFrame que foi 
# especificado à direita.
# =============================================================================

# =============================================================================
# A operação de left join retorna todas as linhas do DataFrame especificado 
# à esquerda no comando merge(), mesmo que não exista casamento 
# (valor equivalente) no DataFrame à direita. Para que o conceito fique claro, 
# vamos retornar para o nosso exemplo envolvendo os DataFrames emp e depto. 
# O empregado "José" não possui um departamento cadastrado (o atributo idDepto 
# possui valor None para a linha referente a este empregado em emp). 
# Se desejarmos produzir um DataFrame contendo todos os empregados 
# combinados com os dados de seus respectivos departamentos, mas que também 
# inclua os empregados sem departamento cadastrado, é preciso fazer uso do 
# left join como mostrado a seguir: 
# =============================================================================
    
j_esq = pd.merge(emp, depto, how="left", left_on="idDepto", right_on="id")

# =============================================================================
# O parâmetro how="left" é usado para indicar à pandas que se deseja realizar 
# o left join.
# =============================================================================

# =============================================================================
# A junção do tipo right join retorna todas as linhas do DataFrame à direita, 
# mesmo que não exista casamento (valor equivalente) no DataFrame à esquerda.
# Desta forma, para produzir um DataFrame com todos os empregados combinados
# com os dados de seus departamentos, mas incluindo os empregados sem 
# departamento cadastrado, seria necessário montar o merge() da forma 
# indicada a seguir, invertendo a posição de empe depto.
# =============================================================================

j_dir = pd.merge(depto, emp, how="right", left_on="id", right_on="idDepto")

# =============================================================================
# O parâmetro how="right" é usado para indicar à pandas que se deseja realizar 
# o right join. Embora o resultado seja conceitualmente equivalente ao do 
# left join, uma diferença é que no DataFrame resultante os dados vindos de
# depto são colocados antes daqueles vindos de emp, uma vez que depto foi
# especificado antes de emp no merge().
# =============================================================================

j_full = pd.merge(emp, depto,how="outer", left_on="idDepto", right_on="id")

flags = pd.read_csv("flags.csv")
countries = pd.read_csv("countries.csv")


num_linhas_flags = flags.shape[0]
num_linhas_countries = countries.shape[0]

# Junção interna: países comunsa ambas as bases;
ambas = pd.merge(flags, countries, how="inner", left_on="name",
                 right_on="country")

num_linhas_ambas = ambas.shape[0]

# left join: países apenas em flags;
so_flags = pd.merge(flags, countries, how="left",
                    left_on="name", right_on="country")
so_flags = so_flags[pd.isnull(so_flags['country'])==True]
num_linhas_so_flags = so_flags.shape[0]

# Right Join: países apenas em countries
so_countries = pd.merge(flags, countries, how="right",
                        left_on="name", right_on="country")
so_countries = so_countries[pd.isnull(so_countries['name'])==True]
num_linhas_so_countries = so_countries.shape[0]

print('- Num países em "flags":', num_linhas_flags) 
print('- Num países em "countries":', num_linhas_countries) 
print('- Num países em ambas:', num_linhas_ambas) 
print('- Num países só em "flags":', num_linhas_so_flags) 
print('- Num países só em "countries":', num_linhas_so_countries) 
print('------------------------------')
print("países só em flags:")
print(so_flags['name'])
print('------------------------------')
print("países só em countries:")
print(so_countries['country'])


# =============================================================================
# o left join foi efetuado em conjunto com a indexação booleana para que 
# fosse possível determinar os países presentes apenas em flags:
# =============================================================================

# =============================================================================
# Nela, o right join e a indexação booleana são empregados para determinar 
# os países que estão apenas no DataFrame countries (aqueles que ficam 
# com valor null para o atributo name depois da execução do right join).
# =============================================================================

# =============================================================================
# Na terceira parte do programa, todos os resultados computados são impressos, 
# incluindo a listagem completa de países que fazem parte apenas de flags e 
# dos que fazem parte apenas de countries.
# =============================================================================















