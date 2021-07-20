# -*- coding: utf-8 -*-
"""
Livro pandas;
Capítulo 6 - Limpeza e Trnaformação de DataFrames
"""
# =============================================================================
# A seleção consiste na operação que gera um novo DataFrame a partir da 
# extração de algumas linhas de interesse de um outro DataFrame. 
# Essa operação também é conhecida como filtragem de linhas.
# =============================================================================

# =============================================================================
# Embora os DataFrames possam ser filtrados com o emprego de diferentes 
# técnicas, a mais utilizada na prática é a indexação booleana, 
# provavelmente por ser mais intuitiva. Nesta abordagem, passamos uma 
# Series de elementos booleanos (True/False) para o DataFrame, com o
#  objetivo de obter apenas as linhas associadas ao valor True. 
#  No programa a seguir, a técnica é empregada para listar os países 
#  da Oceania que fazem parte da base flags.
# =============================================================================


import pandas as pd

# Importando a base de dados;
flags = pd.read_csv("flags.csv")

# Selecionando apenas paises da Oceania;
v = (flags["landmass"]==6)
flags_oceania = flags[v]

# Imprimindo dados;
print(flags_oceania)

# =============================================================================
# v = (flags['landmass']==6): gera uma Series chamada v, de elementos 
# booleanos, que associará o valor True às linhas onde landmass possui 
# o valor 6. Veja que o teste de igualdade é realizado com o uso do 
# operador == (dois símbolos de = e não apenas um!); 
# flags_oceania = flags[v]: comando de atribuição que gera o DataFrame 
# flags_oceania. Este conterá apenas as linhas em que v é True.
# =============================================================================

# Abaixo vamos refatorar o código anterior;
flags_oceania = flags[flags['landmass']==6]
print(flags_oceania)

# =============================================================================
# A seguir, são apresentados e comentados diversos exemplos de utilização 
# prática para os operadores lógicos e de comparação. Substitua a condição 
# (flags['landmass']==6) por cada um dos exemplos adiante para que você possa 
# executá-los e verificar os resultados retornados. 
# (flags['landmass']!=6): países que não são da Oceania; 
# (flags['colours'] <=2): países com no máximo 2 cores em sua bandeira; 
# (flags['language'] ==1) | (flags['language'] ==4): países cujo idioma 
# predominante é o inglês ou o alemão; 
# (flags['landmass'] ==6) & (flags['area'] >200): países da Oceania, 
# com área acima de 200 mil quilômetros quadrados. 
# (flags['landmass'] ==6) & (flags['area'] >200) & (flags['language'] ==1): 
# países da Oceania, com área acima de 200 mil quilômetros quadrados, 
# em que o idioma predominante é o inglês.
# =============================================================================

# PROJEÇÃO;
# =============================================================================
# A projeção é a operação que gera um novo DataFrame a partir da extração de 
# algumas colunas de um outro DataFrame. É uma operação ainda mais simples 
# do que a seleção, uma vez que para implementá-la basta especificar uma 
# lista de nomes de atributos. No exemplo a seguir, a projeção é utilizada 
# para extrair apenas as colunas name,colours,language,landmass e area dos 
# países da Oceania com área acima de 200 mil quilômetros quadrados.
# =============================================================================

import pandas as pd

# Importando base de dados;
flags = pd.read_csv("flags.csv")

# Selecionando apenas linhas de paises da Oceania com área acima de 200 mil
# km quadrados;
v = (flags['landmass']==6) & (flags['area'] > 200)
df = flags[v]

print(df)

# RECRIANDO OS INDICES;
import pandas as pd

flags = pd.read_csv("flags.cvs")

# Selecionando apenas linhas de paises da Oceania com área acima de 200 mil
# km quadrados;
v = (flags['landmass']==6) & (flags['area'] > 200)
df = flags[v]
df = df[['name', 'colours', 'language', 'landmass', 'area']]

# Realizando o reset;
df = df.reset_index(drop=True)
print(df)


# =============================================================================
# O parâmetro drop=True é utilizado para evitar que a pandas gere uma 
# coluna extra com o índice anterior.
# Para maiores informações sobre o método reset_index(), consulte o link a 
# seguir: 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html.
# =============================================================================

# MODIFICAÇÃO DE DADOS;
# Inserção;

# =============================================================================
# Inserção consiste na operação de inserir um ou mais objetos (novas linhas) 
# em um DataFrame. Na pandas, essa tarefa é realizada de maneira trivial: 
# basta especificar os dados dos objetos em um novo DataFrame e depois 
# utilizar o método concat() para concatená-lo ao DataFrame alvo da 
# modificação. No exemplo a seguir, mostramos como o processo é feito 
# para inserir os dados do país "East Timor" (Timor Leste) no DataFrame 
# flags:
# =============================================================================

import pandas as pd

flags = pd.read_csv("flags.csv")

# Criando novo DF;
df_novo = pd.DataFrame(
 {
 'name': 'East Timor',
 'landmass': 5,
 'area': 15,
 'language': 10,
 }, index=[0])

# Inserindo um novo país em flags;
flags = pd.concat([flags,df_novo], ignore_index=True, sort=False)

# Imprimindo o DF alterado;
print(flags[['name',
 'landmass',
 'area',
 'language',
 'religion'
 ]])

# ATUALIZAÇÃO;
# =============================================================================
# Atualização consiste na operação de alterar os valores de alguns atributos 
# de um objeto existente. Para alterar um atributo específico de uma linha 
# através de seu índice, basta utilizar o método at(). No exemplo a seguir, 
# o valor do atributo religion é alterado para 0 na linha referente ao 
# Timor Leste (índice=194).
# =============================================================================

flags.at[194,'religion']=0

# =============================================================================
# Entretanto, utilizar o valor do índice para guiar a operação de modificação 
# nem sempre é possível ou simples. Por exemplo, a posição do "Timor Leste" 
# pode facilmente mudar de 194 para um outro valor caso objetos sejam 
# removidos ou inseridos em flags e, em seguida, o DataFrame seja reindexado.
# =============================================================================

# =============================================================================
# Uma alternativa mais viável é realizar a alteração tendo por base um atributo 
# que funcione como uma chave de identificação para os registros da base de 
# dados. No caso de flags, a chave é o atributo name, pois é este o atributo 
# que identifica unicamente cada país. No programa a seguir, mostramos como 
# aplicar o método loc() para efetuarmos uma atualização com base no atributo 
# name.
# =============================================================================

# Atualização;
import pandas as pd

flags = pd.read_csv("flags.csv")

# Criando um DF com dados do novo país;
df_novo = pd.DataFrame(
 {
 'name': 'East Timor',
 'landmass': 5,
 'area': 15,
 'language': 10,
 }, index=[0])

# Inserindo novo país em flags;
flags = pd.concat([flags, df_novo], ignore_index=True, sort=False)

# Atualizando o valor do atributo "religion";
flags.loc[flags['name']=='East Timor', 'religion'] = 0

# Imprimndo DF alterado;
print(flags[['name',
 'landmass',
 'area',
 'language',
 'religion'
 ]])


# =============================================================================
# A atualização através do método loc() foi feita através da seguinte sintaxe: 
# loc(teste, atributo)=valor
# Primeiro especifica-se um teste lógico para identificar as linhas que 
# serão atualizadas. Em nosso exemplo, o teste especificado foi 
# flags['name']=='East Timor', que retorna True para uma única linha. 
# Após o teste lógico, deve-se indicar o atributo (ou lista de atributos) 
# que serão modificados. Em nosso exemplo, apenas religion. Por fim, 
# você deve especificar o valor a ser atribuído (ou lista de valores) 
# após o sinal de =.
# =============================================================================

# EXCLUSÃO;

# =============================================================================
# Exclusão consiste na operação de remover um ou mais objetos de um DataFrame. 
# Se você conhece de antemão os índices dos objetos a serem excluídos, então 
# a operação pode ser feita de maneira trivial, com o uso do método drop(). 
# Por exemplo, para remover os objetos de índice 1, 5 e 193 de flags e depois 
# resetar os índices do DataFrame, basta utilizar o método drop() seguido do 
# reset_index(), da forma mostrada a seguir:
# =============================================================================

flags = flags.drop([1, 5, 193])
flags = flags.reset_index(drop=True)

# =============================================================================
# Entretanto, no caso mais comum — onde objetos são excluídos com base no 
# valor de um ou mais atributos — utilizamos o método loc(). Porém, é preciso 
# muita atenção, pois devemos criar um teste lógico para determinar os objetos 
# que deverão permanecer no DataFrame e não os que vão sair. Observe o exemplo 
# a seguir, que remove todos os países que não possuem as cores verde, 
# amarelo, azul e branco em suas bandeiras (só os que possuem todas elas é 
# que não serão excluídos).
# =============================================================================

# EXCLUSÃO;
import pandas as pd

flags = pd.read_csv("flags.csv")

# Mantendo apenas países com cores verde e amarelo;
# azul e branco na bandeira;

flags = flags.loc[(flags['green']==1) & 
 (flags['gold']==1) & 
 (flags['blue']==1) &
 (flags['white']==1)]

print(flags[['name',
 'green',
 'gold',
 'blue',
 'white']])

Neste exemplo, utilizamos o método loc() para remover de flags todos 
os países cujo resultado do teste lógico seguinte resulta em False: 

(flags['green']==1) & (flags['gold']==1) & (flags['blue']==1) & (flags['white']==1)

# SUBSTITUINDO VALORES;

# =============================================================================
# O método replace() pode ser utilizado em situações onde se deseja formatar 
# uma coluna através da substituição de certos valores por um outro conjunto 
# de valores. Por exemplo, no programa a seguir, mostramos como empregar esta 
# técnica para modificar a coluna green, trocando o valor 0 por "Não" e o 
# valor 1 por "Sim".
# =============================================================================

import pandas as pd

# importando base de dados;
flags = pd.read_csv('flags.csv')

# Usando replace();
flags['green'] = flags['green'].replace([0,1],['Não','Sim'])

# Imprimindo DF alterado;
print(flags[['name','green']])

# =============================================================================
# Na sintaxe do replace() primeiro especifica-se a lista de valores que serão 
# substituídos (nesse exemplo, [0,1]) e depois a lista com os novos valores 
# (['Não','Sim']). Note ainda que a substituição é feita a partir de uma 
# atribuição, isto é a coluna green de flags, no lado esquerdo da atribuição, 
# recebe o resultado do replace() especificado no lado direito:
# =============================================================================


# Limpeza de dados;

# =============================================================================
# O método replace() também é muito utilizado para realizar a limpeza de bases 
# de dados. Por exemplo, considere o caso — muito comum! — de uma base de dados 
# CSV que adota um valor sentinela (código especial) para representar dados 
# ausentes, por exemplo, 999999 (outros sentinelas muito usados são -1, 999 
# e -999). Suponha que esta base de dados tenha sido importada para um 
# DataFrame df e que x é o nome da coluna que utiliza o valor sentinela. 
# Para substituir todos os valores 999999 por NaN em x basta utilizar o 
# seguinte comando: df['x'] = df['x'].replace(999999,np.nan)
# =============================================================================

import pandas as pd
import numpy as np

# =============================================================================
# O MÉTODO REPLACE() O método replace() é extremamente rico e possui muitas 
# variações, suportando inclusive o uso de expressões regulares. Consulte a 
# documentação do método para maiores detalhes: 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html.
# =============================================================================

# =============================================================================
# Formatando valores Considere agora que você não deseja substituir valores de 
# uma coluna, mas sim formatá-los. Por exemplo: converter os nomes de todos 
# os países para caixa alta. Situações deste tipo podem ser resolvidas de 
# maneira extremamente simples com o uso do método apply(), que permite que 
# qualquer função do Python seja aplicada de uma só vez sobre todos os 
# valores de uma coluna.
# =============================================================================


# FORMATANDO VALORES;
import pandas as pd

flags = pd.read_csv('flags.csv')

# utilizando o apply();
flags['name'] = flags['name'].apply(str.upper)

print(flags)

# =============================================================================
# O mais interessante do método apply() é que ela aceita o uso de qualquer 
# tipo de função, seja uma função do Python padrão (como upper()) seja uma 
# função definida pelo próprio programador, como será visto já a partir da 
# próxima seção.
# =============================================================================

# =============================================================================
# Discretização é a tarefa de transformação de dados que consiste em converter 
# os valores de um atributo contínuo em um conjunto reduzido de valores 
# discretos ou categóricos. Esta seção cobre a abordagem básica para 
# discretização, baseada na criação de uma função customizada.
# =============================================================================

# CRIANDO FUNÇÃO;
def classe_area(area):
    if area < 10:
        return 'F'
    elif area >= 10 and area < 50:
        return 'E'
    elif area >= 50 and area < 100:
        return 'D'
    elif area >= 100 and area < 500:
        return 'C'
    elif area >= 500 and area < 1000:
        return 'B'
    else:
        return 'A'
    
print('Classe de extensão territorial: ')    
print('Brasil     :', classe_area(8515))
print('Moçambique :', classe_area(801))
print('Portugal   :', classe_area(92))
print('Timor Leste:', classe_area(14))

# =============================================================================
# Uma vez a função tendo sido definida, ela pode ser utilizada em qualquer 
# parte do programa. E é exatamente isto que fizemos! No exemplo, a função 
# classe_area() é chamada quatro vezes, para classificar os países Brasil, 
# Moçambique, Portugal e Timor Leste.
# =============================================================================

# Aplicando funções;

import pandas as pd

def classe_area(area):
    if area < 10:
        return 'F'
    elif area >= 10 and area < 50:
        return 'E'
    elif area >= 50 and area < 100:
        return 'D'
    elif area >= 100 and area < 500:
        return 'C'
    elif area >= 500 and area < 1000:
        return 'B'
    else:
        return 'A'
    
flags = pd.read_csv("flags.csv")

# utilizando a função apply()
flags['classe_area'] = flags['area'].apply(classe_area)

print(flags[['name', 'area', 'classe_area']])


# =============================================================================
# Neste exemplo, utilizamos o método apply() para aplicar a nossa função 
# personalizada classe_area(): 
#     flags['classe_area'] = flags['area'].apply(classe_area)
# Adicionalmente, veja que o programa também exemplificou um processo 
# construção de atributo. Isso porque criamos um novo atributo no DataFrame 
# flags, denominado classe_area, cujo valor foi definido a partir do resultado 
# do apply().
# =============================================================================


# =============================================================================
# DISCRETIZAÇÃO: TÉCNICAS NÃO-SUPERVISIONADAS Também é possível realizar a 
# discretização através dos chamados métodos não-supervisionados. Neste tipo 
# de método, a operação de discretização é feita através da aplicação direta 
# de uma fórmula matemática capaz de determinar automaticamente a configuração 
# de cada faixa de valores. Para maiores informações consulte o link: 
#     https://www.saedsayad.com/unsupervised_binning.htm.
# =============================================================================

# NORMALIZAÇÃO

# =============================================================================
# No entanto, diversos algoritmos de ciência de dados (especialmente algoritmo 
# para cálculo de similaridade ou distância entre objetos) requerem que todos 
# os atributos numéricos estejam na mesma escala para que possam funcionar
# corretamente, ou seja, que estes atributos estejam normalizados dentro de 
# uma faixa de valores comum como [0.0, 1.0] ou [-1, 1]. Isto deve ser feito 
# para assegurar que os números grandes não "dominem" os números pequenos 
# durante a análise.
# =============================================================================

# =============================================================================
# Existem diversas fórmulas que podem ser utilizadas para mapear todos os 
# valores de um atributo para a faixa [0.0, 1.0]. Uma das mais simples é 
# apresentada a seguir. Ela pode ser utilizada sobre qualquer atributo que 
# armazene valores contínuos positivos. 
# valor_normalizado = (x-min(X))/(max(X)-min(X))
# =============================================================================

# =============================================================================
# Nesta fórmula, considere que x e o valor real do atributo numérico X em uma 
# dada linha do DataFrame. Por sua vez, min(X) e max(X) consistem, 
# respectivamente, no menor e no maior valor de X em toda a base de dados. 
# A fórmula apresentada retornará o valor normalizado de x, isto é o valor 
# convertido para algum número localizado entre 0 e 1. No exemplo a seguir, 
# mostra-se uma aplicação prática da fórmula: ela é empregada para computar 
# o valor normalizado do atributo area de todos os países de flags.
# =============================================================================

import pandas as pd

flags = pd.read_csv('flags.csv')

# Normalizando area;
area_max = max(flags['area'])
area_min = min(flags['area'])
flags['area_norm'] = (flags['area'] - area_min) / (area_max - area_min)

print(flags[['name', 'area', 'area_norm']])


# =============================================================================
# # Normalização de atributos categóricos;
# Em uma base de dados, os atributos categóricos costumam apresentar grande 
# variação no número de categorias. Veja a seguir o número de categorias de 
# três diferentes atributos da base de dados flags: religion: 8 categorias 
# language: 10 categorias red: 2 categorias (variável binária)
# =============================================================================

import pandas as pd

flags = pd.read_csv('flags.csv')

# utilizando metodo get_dummies() e join()
dummies = pd.get_dummies(flags['language'], prefix='lg')
flags = flags.join(dummies)
print(flags[["language",
 "lg_1",
 "lg_2",
 "lg_3",
 "lg_4",
 "lg_5",
 "lg_6",
 "lg_7",
 "lg_8",
 "lg_9",
 "lg_10"
 ]])

# =============================================================================
# Neste programa, o método get_dummies() foi utilizado com dois parâmetros: 
# flags['language']: coluna que será transformada; prefix='lg': prefixo dos 
# atributos que serão criados. Como resultado, foi gerado um novo DataFrame 
# chamado dummies, contendo 192 linhas (uma para cada país) e 10 atributos
# binários, lg_1 a lg_10, um para cada categoria de language:
# =============================================================================

# =============================================================================
# Em seguida, o método join() foi empregado para fazer a junção de dummies 
# com flags, isto é, para incorporar as novas variáveis binárias ao DataFrame 
# flags. Conforme comentado no capítulo anterior, o método join() serve para 
# realizar a junção de DataFrames através dos índices dos mesmos. Melhor 
# explicando: quando usamos o método join(), os índices são utilizados como 
# chave de ligação para combinar o par de DataFrames.
# =============================================================================

import pandas as pd

flags = pd.read_csv('flags.csv')

#(2)-Conversão dos atributos do Grupo 2  
#    De: Categóricos não binários  
#    Para: Categóricos binários

for c in flags.columns:
    if c in ['landmass', 'zone', 'language', 'religion', 'mainhue',
             'topleft', 'botright']:
        dummies = pd.get_dummies(flags[c], prefix=c)
        flags = flags.join(dummies)

#(3)-Normalização dos atributos dos Grupo 3 e 4  
#    De: Numéricos contínuos e discretos  
#    Para: Numéricos com valores na faixa entre 0 e 1

for c in flags.columns: 
    if c in ['area', 'population',
             'bars', 'stripes', 'colours',
             'circles', 'crosses', 'saltires',
             'quarters', 'sunstars']:
        c_max = max(flags[c])
        c_min = min(flags[c])
        flags[c] = (flags[c] - c_min) / (c_max - c_min)

#4-Exclusão dos atributos indesejados 

flags = flags.drop(columns=['name', 'landmass',
                            'zone', 'language',
                            'religion', 'mainhue',
                            'topleft', 'botright',])

#5-imprime a configuração final de flags  
#imprime as primeiras linhas
print('head():'); print(flags.head())
print('-----------------------------------------------')

#imprime as últimas linhas
print('tail():'); print(flags.tail())
print('-----------------------------------------------')

#6-Salva o dataset alterado para um arquivo 
flags.to_csv("flags_transf.csv", sep=",", index=False)

# =============================================================================
# O programa é dividido em 6 partes e utiliza algumas das técnicas que foram 
# introduzidas ao longo deste capítulo, sem qualquer tipo de modificação. 
# Aplicamos diretamente e tudo funcionou! A seguir, a explicação relativa a 
# cada parte do programa. A primeira parte consiste simplesmente na importação 
# do dataset flags.  Na segunda parte, fazemos a conversão de todos os 
# atributos do Grupo 2. Isto é: cada atributo categórico com k>2 categorias 
# é transformado em k atributos binários. Por exemplo, language, é transformado 
# em language_1 ... language_10. Para tal, bastou empregar o
# método get_dummies() em parceria com o método join(). De maneira análoga, 
# na parte 3, todos os atributos numéricos, sejam contínuos ou discretos, 
# são normalizados para valores entre 0 e 1. Utilizamos a mesma fórmula que 
# foi apresentada no tópico sobre normalização. A parte 4 é bastante 
# interessante. Ela tem por objetivo eliminar do DataFrame todos os atributos 
# indesejados. Por exemplo, depois de gerar os atributos 
# language1 ... language10, não faz mais nenhum sentido continuar com o 
# atributo original language. Então, utilizamos o método drop() passando uma 
# lista contendo language e todos os demais atributos que se tornaram inúteis 
# após a transformação da base. É importante comentar que aproveitamos para 
# também eliminar o atributo name, que é a chave identificadora dos registros 
# de flags (conforme comentado no capítulo 1 deste livro, os atributos chave 
# não são úteis para a construção de modelos de Machine Learning). 
# Na parte 5, imprime-se a nova configuração de flags.  
# Por fim, na parte 6, o arquivo transformado é salvo para um CSV chamado 
# flags_transf.csv.
# =============================================================================
































































