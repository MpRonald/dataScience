# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:22:20 2020

Capítulo 04 -> Conhecendo seus Dados
"""

# =============================================================================
# Tipos de atributos:
#             
#     numérico  -> contínuo  
#               -> discreto
# 
#     categórico -> nominal
#                -> ordinal
# 
# =============================================================================

import pandas as pd

dados = {"renda": [6.46, 1.50, 0.00, 
                   2.57, 9.90, 6.22],
         "empregos": [1,1,0,1,2,3],
         "sexo": ["F","M","F","M","M","F"],
         "escolaridade": ["pós-graduação","fundamental",
                          "médio","médio",
                          "superior","médio"]
 }

pme = pd.DataFrame(dados)

# imprimindo o nome de cada atributo e seu dtype;
print(pme.dtypes)

# =============================================================================
# Um objeto (linha do DataFrame) pode também ser chamado de 
# observação, instância, exemplo, registro, tupla ou data point. Por sua vez, 
# um atributo (coluna do DataFrame) pode também ser chamado de variável, 
# feature, dimensão ou data field. Muitas vezes, um conjunto de atributos que 
# descreve um dado objeto é chamado de attribute vector ou feature vector.
# =============================================================================

# ESTATISTICAS BÁSICAS;
# Medidas de tendência central:
# =============================================================================
"""Uma medida de tendência central é aquela capaz de representar o que é médio 
 ou típico do conjunto de dados."""
# =============================================================================

# =============================================================================
# # MEDIANA:
 """Agora vamos falar da mediana. A ideia desta medida é separar a distribuição 
 em duas partes iguais. A mediana corresponderá ao ponto do meio."""    
# =============================================================================

# =============================================================================
# # MODA:
 """Já a moda consiste no valor mais frequente em uma distribuição. 
 Por exemplo, pesquisas recentes indicam que, na área de ciência de dados, 
 há mais programadores Python do que adeptos de qualquer outra linguagem de 
 programação. Desta forma Python é a moda entre as linguagens de programação.
 """    
# =============================================================================

# =============================================================================
# No Pandas utilizamos os seguintes métodos:
#     média => mean()
#     mediana => median()
#     moda => mode()
# =============================================================================

import pandas as pd

#Estatísticas básicas: medidas de tendência central

dados = {"jogador": ["Marcelo", 
                     "Pedro",
                     "Marcelo", 
                     "Adriano",
                     "Mauro", 
                     "Pedro",
                     "Marcelo"],
         "infracao": ["FALTA VIOLENTA", 
                      "RECLAMACAO",
                      "FALTA COMUM",
                      "RECLAMACAO",
                      "FALTA COMUM",
                      "FALTA VIOLENTA",
                      "RECLAMACAO"],
         "punicao": [4,1,3,2,4,4,2]
 }
df = pd.DataFrame(dados)

#calcula as medidas de tendência central

print("Média: ", df['punicao'].mean())
print("Mediana: ", df['punicao'].median())
print("Moda: ", df['punicao'].mode().values)

# =============================================================================
# Veja que, no exemplo, a forma de utilizar os métodos mean() e median() foi 
# bastante direta: bastou escolher a coluna-alvo (df['punicao']) e depois 
# "plugar" o nome do método. Isso porque esses métodos retornam um valor escalar 
# (um número). Já o método mode() é um pouquinho mais chato para se trabalhar, 
# pois ele sempre retorna uma Series em vez de um escalar. Isso porque uma 
# distribuição pode ser unimodal (possui uma moda), bimodal (possui duas modas) 
# ou multimodal (apresenta várias modas).
# Por isso, nosso programa imprime apenas o values dessa Series, que contém 
# o valor escalar 4.
# =============================================================================


# =============================================================================
# média  -> contínuo e discreto   
# mediana -> contínuo e discreto   
# moda -> discreto, nominal e ordinal
# =============================================================================


# =============================================================================
# # Medidas de Variabilidade:
# Serão apresentadas três medidas deste tipo: amplitude, variância 
# e desvio padrão.
# =============================================================================

# =============================================================================
# Amplitude é uma medida rápida da variabilidade. Ela consiste na diferença 
# entre o mais alto e o mais baixo valor de um determinado conjunto de dados. 
# Em nosso exemplo, a amplitude do Juiz A é igual a 3, pois a sua maior 
# punição foi de 4 jogos e a menor de 1 jogo (4 – 1 = 3). Já a amplitude do 
# Juiz B é igual a 5, pois a sua maior punição foi de 6 jogos e a menor de 1 
# jogo (6 – 1 = 5). Com isto, já fica claro que a distribuição das punições 
# do Juiz B apresenta uma maior variabilidade do que a do Juiz A.
# =============================================================================

# =============================================================================
# CALCULO DE VARIANCIA:
#     Juiz A
#  (4 - 2,86)² =  1,30
#  (1 - 2,86)² =  3,46
#  (3 - 2,86)² =  0,02
#  (2 - 2,86)² =  0,74
#  (4 - 2,86)² =  1,30
#  (4 - 2,86)² =  1,30
#  (2 - 2,86)² =  0,74
#  soma =  8,86
#  variância = (8,86 / 6) = 1,48
# =============================================================================

# =============================================================================
# Cálculo da variância das penas do Juiz B
#  (2 - 2,86)² =  0,74
#  (1 - 2,86)² =  3,46
#  (4 - 2,86)² =  1,30
#  (1 - 2,86)² =  3,46
#  (1 - 2,86)² =  3,46
#  (5 - 2,86)² =  4,58
#  (6 - 2,86)² =  9,86
#  ------------------
#  soma        = 26,86
#  variância = (26,86 / 6) = 4,48
# =============================================================================

# =============================================================================
# A variância considera todos os valores da distribuição, oferecendo uma 
# vantagem sobre amplitude, que considera somente dois valores. No entanto, 
# um problema associado a esta medida é a sua interpretação difícil. Como os 
# valores dos desvios são elevados ao quadrado, a unidade original de medida 
# acaba sendo alterada. Em nosso exemplo é alterada de "número de jogos" para 
# "número de jogos ao quadrado". Ou seja, o valor 4,48 para a variância 
# significa "punição de 4,48 jogos ao quadrado".
# =============================================================================

# =============================================================================
# Corrigir esse problema é muito simples: basta utilizar a medida de desvio 
# padrão. Essa medida corresponde a nada mais do que a raiz quadrada da 
# variância. Ela é usada exatamente para colocar o valor da variabilidade 
# na unidade original. Ou seja, o desvio padrão das penas do Juiz A é dado 
# por raiz de 1,48 = 1,22 jogo. Para o Juiz B temos raiz de 4,48 = 2,12 jogos. 
# A interpretação que podemos dar para estes valores é a seguinte: em média, 
# as penas atribuídas pelo Juiz A se afastam da média por apenas 1,22 jogo. 
# Já no caso do Juiz B, em média, suas penas se afastam da média por mais 
# de 2 jogos (2,12). Isso indica claramente que as penas do Juiz B apresentam 
# maior variabilidade.
# =============================================================================

# Estatísticas básicas: medidas de variabilidade

import pandas as pd

dados = {"jogador": ["Marcelo", 
                     "Pedro",
                     "Marcelo", 
                     "Adriano",
                     "Mauro", 
                     "Pedro",
                     "Marcelo"],
         "infracao": ["FALTA VIOLENTA", 
                      "RECLAMACAO",
                      "FALTA COMUM",
                      "RECLAMACAO",
                      "FALTA COMUM",
                      "FALTA VIOLENTA",
                      "RECLAMACAO"],
         "juiz_A": [4,1,3,2,4,4,2],
         "juiz_B": [2,1,4,1,1,5,6]
 }

df = pd.DataFrame(dados)

print("Juiz A")
print("Amplitude: ", df['juiz_A'].max() - df['juiz_A'].min())
print("Variância: ", df['juiz_A'].var())
print("Desvio Padrão: ", df['juiz_A'].std())

print("="*50)

print("Juiz B")
print("Amplitude: ", df['juiz_B'].max() - df['juiz_B'].min())
print("Variância: ", df['juiz_B'].var())
print("Desvio Padrão: ", df['juiz_B'].std())

# =============================================================================
# =============================================================================

# =============================================================================
# BOXPLOT:
# Boxplot é uma técnica gráfica popularmente utilizada para exibir vários 
# aspectos de um conjunto de dados. Para explicar as suas características e 
# apresentar a maneira como podemos gerar este tipo de gráfico na pandas, 
# utilizaremos os dois conjuntos de dados a seguir. Considere que eles 
# armazenam os resultados de um experimento que mediu o tempo de espera, 
# em minutos, de dez diferentes homens e mulheres que discaram para uma 
# linha telefônica de um serviço falso de telepromoções (suponha que o 
# atendente os pedia para aguardar e nunca mais retornava).
# =============================================================================



# Boxplot - comparação de distribuições

homens = [4, 2, 7, 3, 1, 4, 2, 4, 8, 1]
mulheres = [5, 4, 6, 5, 4, 2, 6, 6, 4, 3]

import pandas as pd

df = pd.DataFrame({"homens":[4, 2, 7, 3, 1, 4, 2, 4, 8, 1],
                   "mulheres": [5, 4, 6, 5, 4, 2, 6, 6, 4, 3]})

boxplot = df.boxplot(column=['homens', 'mulheres'], showmeans=True)

# =============================================================================
# Para gerar o boxplot, basta utilizar o método boxplot(), especificando uma 
# relação de colunas numéricas (neste exemplo homens e mulheres). Um boxplot 
# será produzido para cada coluna. Mas como interpretar esse gráfico? 
# A explicação é dada a seguir:
# =============================================================================

# =============================================================================
# A caixa retangular dentro do gráfico representa o intervalo entre o 
# primeiro quartil (Q1, linha inferior) e o terceiro quartil 
# (Q3, linha superior). De uma maneira simplificada, podemos dizer que Q1 
# corresponde à mediana dos valores compreendidos entre o menor valor e a 
# mediana do conjunto de dados. Já Q3 corresponde à mediana dos valores 
# compreendidos entre a mediana e o maior valor do conjunto de dados. 
# A discreta reta através da caixa mostra a mediana 
# (3.5 para os homens e 4.5 para as mulheres). A mediana também é chamada de Q2. 
# O pequeno triângulo no meio da caixa é a média (3.6 para os homens e 4.5 para 
# as mulheres). É importante observar que, para que a média seja exibida, 
# torna-se preciso utilizar o parâmetro showmeans=True. As duas linhas fora 
# da caixa (chamadas de whiskers) são utilizadas para indicar que os valores 
# localizados fora delas podem ser considerados outliers (valores suspeitos). 
# Ainda neste capítulo, falaremos sobre os outliers e mostraremos outros tipos 
# de gráfico que podem ser gerados com a pandas, tais como gráfico de barras e 
# histogramas.
# =============================================================================


# EIXOS:
# =============================================================================
# Antes de apresentar o exemplo, é importante introduzir o conceito de 
# eixo (axis). Trata-se, basicamente, de uma propriedade que podemos 
# especificar para decidir se queremos produzir estatísticas por coluna 
# (axis=0, que corresponde ao modo padrão) ou por linha (nesse caso, 
# especifica-se axis=1).
# =============================================================================

import pandas as pd

#cria uma DataFrame com as notas de 4 alunos em 3 provas
notas = pd.DataFrame({"A1":[9.8, 7.2, 8.0],
                      "A2": [5.3, 4.0, 3.5],
                      "A3": [5.5, 8.1, 7.2],
                      "A4": [7.0, 7.5, 6.5]}, 
                     index=["P1","P2","P3"])
#imprime o DataFrame
print("\nnotas finais: ")
print('='*40)
print(notas)

print("\nMédia de cada aluno:")
print('*-'*15)
print(notas.mean())

print("\nMédia de cada prova:")
print('*-'*15)
print(notas.mean(axis=1))

print("\nMaior nota de cada prova:")
print('*-'*15)
print(notas.max(axis=1))

# =============================================================================
# Quando fazemos notas.mean(), a pandas computa de forma automática a média 
# dos valores de todas as colunas ("A1", "A2", "A3" e "A4"), o que corresponde 
# à média de cada aluno. Da mesma forma notas.max() computa o maior valor 
# armazenado em cada coluna. Por sua vez, o comando notas.mean(axis=1) faz 
# com que sejam geradas as médias dos valores armazenados em cada linha 
# ("P1", "P2" e "P3"), o que corresponde à média de cada prova. De maneira 
# análoga, notas.max(axis=1) retorna as notas máximas de cada prova. 
# Em resumo: o padrão da pandas é computar estatísticas por colunas. 
# Para computar por linhas, você deve utilizar o parâmetro axis=1.
# =============================================================================

# Ranqueamento e ordenação
# Métodos sort_values() e rank()

import pandas as pd

dados = {"nadador": ["Simonas Bilis",
                     "Benjamin Proud",
                     "Anthony Ervin",
                     "Florent Manaudou",
                     "Andriy Hovorov",
                     "Nathan Adrian",
                     "Bruno Fratus",
                     "Brad Tandy"],
         "nacionalidade": ["Lituânia",
                           "Grã-Bretanha",
                           "Estados Unidos",
                           "França",
                           "Ucrânia",
                           "Estados Unidos",
                           "Brasil",
                           "África do Sul"],
         "tempo": [22.08,
                   21.68,
                   21.40,
                   21.41,
                   21.74,
                   21.49,
                   21.79,
                   21.79]
 }
raias = list(range(1,9))

prova50m = pd.DataFrame(dados, index=raias)
prova50m.index.name = 'raia'

# ordena pelo tempo de forma crescente
prova50m = prova50m.sort_values(by="tempo")
print("Resultado final ordenado por tempo: ")
print(prova50m)

# gera os rankings
resultado_por_raia = prova50m['tempo'].rank(method="min")
print("\nPosição de cada nadador (por raia): ")
print(resultado_por_raia)
 
# =============================================================================
# Agora uma explicação detalhada sobre o programa. Mais uma vez, ele está 
# dividido em três partes. 
# A primeira trata simplesmente de criar e imprimir o DataFrame. O comando 
# prova50m.index.name = 'raia' é usado para atribuir o rótulo raia à coluna 
# que armazena o índice. 
# A segunda parte apresenta o método sort_values(). Este método serve para 
# ordenar o DataFrame por uma ou mais colunas, que devem ser especificadas 
# no parâmetro by. Neste exemplo, by="tempo" foi utilizado para gerar uma 
# ordenação ascendente pela coluna tempo. Uma observação muito importante é 
# que se você quiser mudar de fato o DataFrame (ou seja, ordená-lo de verdade 
# em vez de apenas exibir as suas linhas ordenadas), precisará fazer uso de 
# um comando de atribuição:
# =============================================================================

prova50m = prova50m.sort_values(by="tempo")
print(prova50m)

# =============================================================================
# A ordenação default é ascendente. Para ordenar de forma descendente, 
# você deve utilizar o parâmetro ascending=False.
# =============================================================================

prova50m = prova50m.sort_values(by="tempo", ascending=False)
print(prova50m)

# =============================================================================
# Para ordenar por mais de uma coluna, é preciso especificá-las em uma lista. 
# Por exemplo, by=["tempo","nacionalidade"] faria com que a pandas realizasse 
# a ordenação por tempo (primeiro critério) e, em casos de empate, por país 
# (segundo critério).
# =============================================================================

prova50m = prova50m.sort_values(by=["tempo","nacionalidade"], ascending=False)
print(prova50m)


# =============================================================================
# A terceira e última parte do programa apresenta o método rank() que serve 
# para gerar uma Series contendo ranking de valores:
# =============================================================================

resultado_por_raia = prova50m['tempo'].rank(method="min")
print(resultado_por_raia)

# =============================================================================
# O parâmetro method="min" serve para especificar o procedimento a ser 
# adotado para o tratamento de empates. Neste exemplo, os nadadores das 
# raias 7 e 8 empataram em sexto lugar e method="min" faz com que a posição 
# 6 seja atribuída para ambos. Outros valores possíveis seriam method="max" 
# (7 seria atribuído para ambos), method="average" (colocaria 6.5 em ambos).
# =============================================================================


# Produzindo tabulações
# Domínio e tabelas de frequência

# =============================================================================
# No programa a seguir introduzimos dois métodos da pandas muito utilizados 
# quando desejamos estudar atributos categóricos como os que acabamos de 
# mencionar. São eles:
# =============================================================================
"""-> unique(): retorna o domínio de um atributo do DataFrame, isto é, 
todas as categorias distintas que ele assume.
-> value_counts(): gera uma tabela de frequências simples para o atributo."""
# =============================================================================

import pandas as pd

dados = {"sexo": ["F","M","F","F","F","M"],
         "bairro": ["Belverde",
                    "Belverde",
                    "Savassi",
                    "Anchieta",
                    None,
                    "Savassi"],
         "valor": [150.00,
                   35.00,
                   80.00,
                   250.00,
                   9.90,
                   25.00],                   
         "cartao": ["Master",
                    "Visa",
                    "Visa",
                    "Amex",
                    "Elo",
                    "Master"]}
id_clientes = [1,2,3,4,5,6]

vendas = pd.DataFrame(dados, index=id_clientes)

# retorna o domínio dos atributos categóricos
print("Domínio dos atributos categoricos")
print("="*30)
print('sexo:', vendas['sexo'].unique())
print('bairro:', vendas['bairro'].unique())
print('cartao:', vendas['cartao'].unique())

# retorna as frequências dos valores de cada coluna
print('Tabelas de frequência:')
print("="*30)
print("\nsexo:")
print(vendas['sexo'].value_counts())
print("\nbairro:")
print(vendas['bairro'].value_counts())
print("\ncartao:")
print(vendas['cartao'].value_counts())

# =============================================================================
# Um detalhe importante sobre o value_counts() é o fato de que ele retorna 
# a tabela de frequências em uma Series.
# =============================================================================

# =============================================================================
# Agregações 
# Agregação é uma operação que visa computar estatísticas para 
# grupos de linhas de um DataFrame. Os grupos de linhas são definidos a 
# partir de valores de um ou mais atributos categóricos, enquanto as 
# estatísticas são computadas sobre atributos numéricos. Na biblioteca 
# pandas, agregações são produzidas com o uso do método group_by().
# =============================================================================


# agregação com o método groupby()

dados = {"sexo": ["F","M","F","F","F","M"],
         "bairro": ["Belverde",
                    "Belverde",
                    "Savassi",
                    "Anchieta",
                    None,
                    "Savassi"],
         "valor": [150.00,
                   35.00,
                   80.00,
                   250.00,
                   9.90,
                   25.00],                   
         "cartao": ["Master",
                    "Visa",
                    "Visa",
                    "Amex",
                    "Elo",
                    "Master"]}
id_clientes = [1,2,3,4,5,6]

vendas = pd.DataFrame(dados, index=id_clientes)

# gera uma variavel "grouped" onde a chave é "bairro" e a medida é "valor";
grupo_valor_bairro = vendas['valor'].groupby(vendas['bairro'])

# computa agregados a partir da variavel gerada;
print("quantidade de clientes por bairro:\n", grupo_valor_bairro.count())
print("valor total de vendas por bairro:\n", grupo_valor_bairro.sum())
print("valor medio de vendas por bairro:\n", grupo_valor_bairro.mean())

# o segredo deste programa esta na linha de codigo groupby()
"""O exemplo que acabamos de mostrar produziu um TABULAÇÃO SIMPLES.
Se voce quiser agregar por mais de um atributo categorico, basta especificar
estes atributos em uma lista, e passar como parametro para o metodo groupby()
"""
grupo_valor_bairro=vendas['valor'].groupby([vendas['sexo'],
                                            vendas['bairro']])

# GRAFICOS:
# Graficos de linhas -> esse é o modelo mais simples dos gráficos;

import pandas as pd

df = pd.DataFrame({"x":list(range(1,11))})
df["y"] = (df.x * 2) + 3
lines = df.plot.line(x="x", y="y", legend=False)

dados = {"óleo de soja:":[71.15, 66.93, 67.91, 67.66],
         "melancia":[10.52, 15.68, 14.95, 26.23],
         "frango congelado":[47.17, 23.68, 38.36, 17.08]
         }

df = pd.DataFrame(dados, index=[3,6,9,12])
lines = df.plot(kind="line", style=[".-","+-","*-"], ylim=(0,100), xlim=(3,12))
# ylim=(0,100) -> escala do eixo y de 0 a 100
# ylim=(3,6,9,12) -> escala do eixo y de 3 a 12

# =============================================================================
# # para uma lista completa consulte:
#     https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot.
# =============================================================================

# GRAFICOS DE BARRAS;

# grafico de barras vertical;
df = pd.DataFrame([70,25,50], index=['teatro', 'escultura', 'pintura'])
barras = df.plot(kind="bar", legend=False)

df = pd.DataFrame({"mulheres":[40,10,30], "homens":[30,15,20]},
                  index=['teatro', 'escultura', 'pintura'])
                  
barras = df.plot(kind="bar", legend=True, color=["yellow","blue"])

# HISTOGRAMA
df = pd.DataFrame({"tempo":[4,5,1,7,7,8,6,6,5,2,5,8,7,1,6,3,4,8,5,7,4,6,3,
                            6,2,6,8]})
hist = df.plot(kind='hist', bins=3)


# DETECÇÃO DE OUTLIERS

# =============================================================================
# Outliers são dados anormais que podem ser reais ou, no caso mais frequente, 
# gerados devido a algum erro (seja um erro na coleta dos dados, um erro de 
# digitação etc.). Outliers costumam exercer influência negativa na qualidade 
# dos resultados de um processo de ciência de dados. Por esta razão, torna-se 
# preciso identificá-los na etapa de estudo da base de dados.
# =============================================================================

# =============================================================================
# QUARTIS
# => Q1 (1o quartil): 25% das observações abaixo, 75% acima. 
# => Q2 (2o quartil): 50% das observações abaixo, 50% acima 
# (ou seja, Q2 é a mediana do conjunto de dados). 
# => Q3 (3o quartil): 75% das observações abaixo, 25% acima.
# =============================================================================

# =============================================================================
# A medida do IQR consiste na diferença entre o terceiro e o primeiro quartis 
# da distribuição (Q3 – Q1). A técnica para detecção de outliers baseada no 
# IQR funciona da seguinte forma: todos os pontos localizados a uma distância 
# de 1,5 x IQR acima do terceiro quartil ou abaixo do primeiro quartil são 
# listados como candidatos a outliers. Como estes pontos se localizam muito 
# distantes de Q1 ou de Q3, há uma grande chance real de eles realmente 
# representarem dados anormais.
# =============================================================================

import pandas as pd

df = pd.DataFrame({"tempo":[4,5,1,7,7,8,6,6,5,2,5,8,7,1,6,3,4,8,5,7,4,6,3,
                            6,2,6,18]})

boxplot = df.boxplot(column=['tempo'], showmeans=True)

# acima podemos ver que o numero 18 é candidato a um outlier;

import pandas as pd

flags = pd.read_csv("flags.csv")

i = 0
for c in flags.columns:
    i += 1
    att = flags[c] # atributo
    att_dtype = att.dtype # dtype
    att_tam_dominio = att.unique().size # tamanho do dominio
    att_tem_nulo = any(att.isnull()) # possui valor nulo?
    
if(att_tam_dominio < 8):
    print("("+str(i)+")atributo:",c, "\t",
          "dtype:", att_dttype, "\t",
          "nulos:", att_tem_nulo, "\n",
          "dominio:", att.unique())
else:
    if(att_dtype == 'object'):
        print("("+str(i)+")atributo:",c, "\t",
          "dtype:", att_dttype, "\t",
          "nulos:", att_tem_nulo, "\n",
          "dominio (primeiros elementos):", att.unique()[0:8])
    else:
        print("("+str(i)+")atributo:",c, "\t",
          "dtype:", att_dttype, "\t",
          "nulos:", att_tem_nulo, "\n",
          "min:", att.min(), "\t",
          "max:", att.max(), "\t",
          "media:", round(att.mean(),2), "\t",
          "d.p:", round(att.std(),2))
        
# =============================================================================
# O programa é dividido em duas partes, a primeira consiste em uma unica linha
# onde o metodo read.csv() é empregado para importar o arquivo flags.csv para
# um DataFrame pandas. A segunda é realizada o estudo dos atributos da base de
# dados, esse trecho funciona da seguinte maneira: primeiro implementamos
# o for, para gerar um laço sobre o nome de todas as colunas, dentro dele
# temos os seguintes comandos:
#     => att = flags[c]: recupera o atributo de nome c; 
#     => att_dtype = att.dtype: recupera o dtype do atributo;  
#     => att_tam_dominio = att.unique().size: utiliza o método unique() para 
#     gerar um vetor contendo o domínio (valores ou categorias distintas) do 
#     atributo. Então o tamanho (número de elementos) deste conjunto 
#     é retornado com a propriedade size. 
#     => att_tem_nulo = any(att.isnull()): a função any() é uma função do 
#     Python padrão que recebe como entrada uma relação de valores 
#     (em uma Series, lista ou outra ED) e retorna True (valor escalar) 
#     caso ao menos um dos elementos da relação seja True.
# =============================================================================

# =============================================================================
# Após obter esses dados, o programa segue o seu processamento e imprime as 
# propriedades básicas do atributo. De acordo com o domínio do atributo 3 
# diferentes tipos de informação poderão ser exibidos: Caso o domínio do 
# atributo possua 8 ou menos elementos, então são impressos todos os seus 
# valores ou categorias. Caso o domínio do atributo possua mais de 8 
# elementos e o seu dtype seja object, são impressas apenas as suas 8 
# primeiras categorias. Caso o domínio do atributo possua mais de 8 elementos 
# e o seu dtype não seja object (ou seja, o atributo é numérico), são 
# impressos os valores mínimo, máximo, médio e o desvio padrão.
# =============================================================================

import pandas as pd

# importa a base de dados:
flags = pd.read_csv("flags.csv")

# gerando tabela de frequencia:
df_cores = pd.DataFrame()

for c in flags.columns:
    if c in ["red","green","blue","gold","white","black","orange"]:
        df_cores[c] = flags[c].value_counts()


print(df_cores)

# a saida acima nos mostra a frequencia com que as cores aparecem;

flags = pd.read_csv("flags.csv")

df_cores = pd.DataFrame()

for c in flags.columns:
     if c in ["red","green","blue","gold","white","black","orange"]:
         df_cores[c] = flags[c].value_counts()

lst_cores = [["red","beige"],["green","beige"],["blue","beige"],
             ["gold","beige"],["white","beige"],["black","beige"],
             ["orange","beige"]]

df_cores.plot(kind='barh', subplots=True, figsize = (8,25),
              color = lst_cores)

# =============================================================================
# Neste programa, utilizamos o método plot() sobre df_cores com os seguintes
# parâmetros: kind='barh': define que o tipo de gráfico é de barras 
# horizontais. subplots=True: para permitir gerar vários gráficos 
# (um para cada cor) dentro de uma única figura.  figsize=(8,25): 
# altura e largura do gráfico.  color = lst_cores: define as cores 
# de cada gráfico. Veja que estamos utilizando sempre a cor bege 
# (beige) na barra referente ao valor 0 (ausência de cor) e a própria 
# cor para a barra que representa o valor 1 (presença da cor).
# =============================================================================
















