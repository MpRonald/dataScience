# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:38:50 2020

Capitulo 3 - Estrutura de Dados DataFrame
"""

import pandas as pd

# criando um DataFrame;
dados = {'nome': ['Argentina','Brasil','França','Itália',
                  'Reino Unido'],
         'continente': ['América','América','Europa','Europa','Europa'],
         'extensao': [2780,8511,644,301,244],'corVerde': [0,1,0,1,0]
 }
siglas = ['AR','BR','FR','IT','UK']
paises = pd.DataFrame(dados,index=siglas)

print(paises)

# =============================================================================
# 
# Observe que cada chave do dicionário foi transformada em uma coluna. As listas 
# associadas às diferentes chaves possuem todas o mesmo tamanho (cinco elementos) 
# e foram utilizadas para estabelecer os dados de cada coluna. 
# 
# Todo DataFrame é um objeto do tipo pandas.core.frame.DataFrame que possui as 
# seguintes propriedades básicas: 
#     *shape: formato do DataFrame, ou seja, o seu número de linhas (shape[0]) e 
#     de colunas (shape[1]); 
#     *index: lista com os rótulos das linhas; 
#     *columns: lista com os rótulos das colunas; 
#     *dtypes: retorna uma Series com os dtypes de cada coluna; 
#     *index.dtype: dtype dos rótulos das linhas.

# =============================================================================

# recupera e imprime propriedades;
num_linhas = paises.shape[0]
num_colunas = paises.shape[1]
indices = paises.index
colunas = paises.columns
paises_tipo = type(paises)
paises_dtypes = paises.dtypes
paises_idx_dtype = paises.index.dtype

print('número de linhas: ', num_linhas)
print('número de colunas: ', num_colunas)
print('rótulos das linhas: ', indices)
print('rótulos das colunas: ', colunas)
print('tipo (type): ',paises_tipo)
print('dtypes das colunas:\n', paises_dtypes)
print('dtype dos rótulos das linhas:', paises_idx_dtype)

# ===== O SHAPE DE UM DATAFRAME ======#

"""
A forma de trabalhar com as propriedades dos DataFrames é muito parecida com a 
das Series. No entanto, a maneira de obter o número de linhas e colunas, com o 
uso da propriedade shape, pode causar alguma confusão. O shape de um DataFrame 
corresponde ao seu formato e é representado como uma tupla bidimensional 
(uma tupla é uma ED praticamente igual a uma lista). O número de linhas é 
armazenado em shape[0] e o de colunas, em shape[1].
"""

# tecnicas para consulta e modificação de dados;
# INDEXAÇÃO;

# =============================================================================
# Utilizamos colchetes [ ] para indexar elementos de um DataFrame. Assim como 
# ocorre com as Series, é possível empregar três técnicas de indexação: 
# indexação tradicional, fatiamento e indexação booleana.
# =============================================================================

# =============================================================================
# -> d.iloc[i][j]   retorna o valor da célula que ocupa a linha i, coluna j   
# -> d.iat[i,j]   retorna o valor da célula que ocupa a linha i, coluna j   
# -> d.iloc[i]['col']   retorna o valor da célula que ocupa a linha i, coluna 
# denominada 'col'   
# -> d.loc['idx'][j]   retorna o valor da célula que ocupa a 
# linha do índice de rótulo 'idx', coluna j   
# -> d.loc['idx']['col']   retorna o valor da célula que ocupa a linha do 
# índice 
# de rótulo 'idx', coluna denominada 'col'   
# -> d.at['idx','col']   retorna o valor da célula que ocupa a linha do índice 
# de rótulo 'idx', coluna denominada 'col'
# =============================================================================

#Busca em DataFrames
import pandas as pd

dados = {'nome': ['Argentina','Brasil','França','Itália',
                  'Reino Unido'],
         'continente': ['América','América','Europa','Europa','Europa'],
         'extensao': [2780,8511,644,301,244],'corVerde': [0,1,0,1,0]
 }
siglas = ['AR','BR','FR','IT','UK']
paises = pd.DataFrame(dados,index=siglas)

# testa se um dado rótulo de linha existe;
tem_BR = 'BR' in paises.index
tem_US = 'US' in paises.index

print(f'Existe o rótulo BR? {tem_BR}')
print(f'Existe o rótulo US? {tem_US}')

# testa se um dado rótulo de coluna existe;
tem_verde = 'corVerde' in paises.columns
tem_azul= 'corAzul' in paises.columns
print(tem_azul)
print(tem_verde)

# testa se um valor faz parte da coluna;
tem_Brasil = paises['nome'].isin(['Brasil'])
tem_Africa = paises['nome'].isin(['Africa'])
print(tem_Brasil)
print(tem_Africa)

# =============================================================================
# Para verificar se um rótulo de linha ou de coluna existe em um DataFrame, 
# você deve aplicar o operador in sobre a lista de rótulos de linha ou de 
# colunas, respectivamente (propriedades index e columns).
# =============================================================================

# =============================================================================
# Se você quiser testar se um valor está armazenado em uma coluna, precisará 
# utilizar o método isin(). Em nosso exemplo, passamos para o método uma lista 
# com um único elemento ('Brasil') e mandamos checar a coluna nome. Como 
# resultado, o método indicou True para a sigla BR.
# =============================================================================

# MODIFICAÇÃO;

import pandas as pd

dados = {'nome': ['Argentina','Brasil','França','Itália',
                  'Reino Unido'],
         'continente': ['América','América','Europa','Europa','Europa'],
         'extensao': [2780,8511,644,301,244],'corVerde': [0,1,0,1,0]
 }
siglas = ['AR','BR','FR','IT','UK']
paises = pd.DataFrame(dados,index=siglas)

# inserindo um novo país;
paises.loc['JP'] = {'nome': 'Japão', 'continente': 'Ásia', 'extensao': 372,
                    'corVerde': 0}
print(dados)

# alterando extensao do Brasil;
paises.at['BR', 'extensao'] = 8512


# removendo Argentina e UK;
paises = paises.drop(['AR', 'UK'])

print('DataFrame após as alterações!')
print(paises)

# =============================================================================
# Para inserir o Japão, bastou indicar os dados desse país em um dicionário e 
# realizar a atribuição com o uso do método loc(). Caso o DataFrame não 
# possuísse rótulos de linha, seria preciso utilizar o método iloc() com o 
# índice da linha a ser inserida.
# =============================================================================

# =============================================================================
# Para alterar uma célula, no caso, a extensão do Brasil, utilizou-se um comando 
# de atribuição simples que empregou o método at() com a indicação dos rótulos 
# de linha e coluna da célula a ser alterada. Caso o DataFrame não possuísse 
# rótulos de linha, seria preciso utilizar o método iat() com o índice da linha 
# a ser alterada.
# =============================================================================

# =============================================================================
# Por fim, para remover linhas, basta utilizar o método drop() indicando a lista 
# de rótulos de linha a serem removidos.
# =============================================================================

# TRABALHANDO COM ARQUIVOS;
# Importação de arquivo CSV;

# =============================================================================
# Podemos realizar a leitura de arquivos CSV (comma-separated values — valores 
# separados por vírgula) e de outros tipos de arquivos baseados em caracteres 
# delimitadores utilizando o método -> read_csv().
# =============================================================================

import pandas as pd
paises = pd.read_csv('paises.csv', index_col = 'sigla')
print(paises)

# =============================================================================
# O método read_csv() é extremamente flexível, possuindo uma série de parâmetros 
# que podem ser utilizados para permitir a importação de arquivos CSV 
# estruturados de diferentes maneiras.
# 
# -sep: caractere ou expressão regular utilizada para separar campos em cada linha; 
# -skiprows: número de linhas no início do arquivo que devem ser ignoradas; 
# -skip_footer: número de linhas no final do arquivo que devem ser ignoradas; 
# -encoding: padrão de codificação do arquivo. A codificação default da pandas 
# é utf-8. Se o seu arquivo estiver codificado no formato ANSI, você deverá 
# utilizar encoding='ansi'. Para obter uma lista completa dos encodings, 
# consulte https://docs.python.org/3/library/codecs.html#standard-encodings; 
# 
# -header: número da linha que contém o cabeçalho (default=0). Se não houver 
# cabeçalho, deve-se especificar header=None ou passar uma lista de nomes 
# através do parâmetro 
# -names; names: permite especificar uma lista de nomes para as colunas; 
# -index_col: permite que uma das colunas seja transformada em índice de linhas; 
# -na_values: sequência de valores que deverão ser substituídos por NA. 
# Útil para transformação de dados; thousands: definição do separador de 
# milhar, por exemplo . ou ,; 
# -squeeze: caso o arquivo CSV possua apenas uma coluna, é possível fazer com 
# que ele seja importado para uma Series em vez de um DataFrame, bastando para 
# isso especificar squeeze=True.
# =============================================================================

import pandas as pd
notas = pd.read_csv('notas.csv', sep=";", names=['matricula',
                                                'nota1', 'nota2'])
print(notas)

# =============================================================================
# O parâmetro sep foi utilizado para definir ; como separador, enquanto names 
# foi empregado para definir os cabeçalhos das colunas.
# =============================================================================

# =============================================================================
# Para que fosse possível colocar matrículas como índices de linha, bastaria 
# ter feito: index_col='matricula'.
# =============================================================================

# Importando um arquivo de serie temporal;

import pandas as pd

# importando um arquivo para um Series;
serie_gols = pd.read_csv('gols.txt', sep=';', squeeze=True, index_col=0)

# convertendo o tipo de indice para datetime e imprime a séria;

serie_gols.index = pd.to_datetime(serie_gols, format='%d/%m/%Y')
print(serie_gols)

# MÉTODO READ_TABLE()

# =============================================================================
# A pandas disponibiliza ainda um outro método para a leitura de arquivos 
# separados por delimitador, denominado read_table(). Este método possui os 
# mesmos parâmetros de read_csv(). A única diferença entre os dois métodos é 
# que o read_csv() tem a vírgula , como separador padrão, enquanto read_table() 
# utiliza a tabulação \t.
# =============================================================================

# Importação de planilhas do Excel;
import pandas as pd

cidades = pd.read_excel('capitais.xlsx')
print(cidades)

# Importação de arquivo JSON;

# =============================================================================
# JSON (JavaScript Object Notation) é um modelo para armazenamento e 
# transmissão de informações no formato texto. Apesar de muito simples, 
# é o mais utilizado por aplicações Web devido à sua capacidade de estruturar 
# informações de forma compacta e autodescritiva.
# =============================================================================

import pandas as pd
import json

with open('notas.json') as f:
    j_notas = json.load(f)


# Tranferindo as informações para um DataFrame;
notas = pd.DataFrame(j_notas, columns=['matricula', 'notas'])
print(notas)

# =============================================================================
# JSON, que consiste em utilizar o método load() do pacote json.
# 
# Na segunda parte, transfere-se o conteúdo do objeto JSON em memória para um 
# DataFrame. É preciso passar duas informações para o construtor padrão: o 
# objeto JSON (j_notas) e a relação de chaves do objeto que desejamos mapear 
# para colunas no DataFrame (utilizando o parâmetro columns).
# =============================================================================

# Salvando um DataFrame em CSV;
# Criando o DataFrame;
dados = {'codigo': [1001,1002,1003,1004,1005],
 'nome': ['Leite','Café','Biscoito','Chá',
 'Torradas']
 }

produtos = pd.DataFrame(dados)

# Salvando o conteúdo para um arquivo;
produtos.to_csv('produto.csv', sep='\t', index=False)

# =============================================================================
# Neste exemplo, realiza-se a gravação do arquivo produtos.csv a partir do 
# conteúdo do DataFrame produtos. Nos parâmetros do método to_csv(), a 
# tabulação \t foi adotada como caractere delimitador (parâmetro sep) e a 
# opção index=False foi utilizada para evitar que os rótulos dos índices 
# (números inteiros) fossem gravados no arquivo.
# =============================================================================

# Para exportar para excel, sua forma seria a seguinte;
produtos.to_excel('rodutos.xlsx', index=False)


# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================

import pandas as pd

flags = pd.read_csv('flags.csv')
print('head():')
print(flags.head()) # imprime primeiras linhas;

print('tails():')
print(flags.tail()) # imprime as ultimas linhas;

# separando cores;
verde = flags['green']
amarelo = flags['gold']
azul = flags['blue']
branco = flags['white']
soma = verde + amarelo + azul + branco

# ferando vetor para as 4 cores
tem_todas = (soma == 4)

# imprime o resultado;
print(flags[tem_todas.values]['name'])

# =============================================================================
# O programa é dividido em três partes. Na primeira, a base flags.csv é 
# importada para um DataFrame chamado flags.
# 
# Na segunda parte, empregamos uma abordagem simples para checar se o arquivo 
# foi importado com sucesso. Ela baseia-se na utilização dos métodos head() e 
# tail().
# 
# Na terceira e mais importante parte do programa, são identificados todos 
# os países que têm verde, amarelo, azul e branco entre as cores da bandeira 
# nacional. O programa funciona da seguinte forma. Primeiro utilizamos o 
# fatiamento para gerar quatro Series, chamadas verde, amarelo, azul e branco, 
# contendo todos os dados das colunas relacionadas a estas respectivas cores 
# (ou seja, a coluna completa com 194 elementos). Lembre-se de que essas 
# colunas são binárias (para cada país, o valor 1 é armazenado se a cor faz 
# parte da bandeira ou 0 caso contrário). Em seguida, utilizamos a computação 
# vetorizada para gerar uma Series chamada soma, cujo conteúdo corresponde à 
# soma verde + amarelo + azul + branco. Desta forma, soma conterá o valor 4 
# apenas nos índices associados aos países que possuem as quatro cores. 
# Logo depois, está o comando fundamental do programa: tem_todas = (soma==4). 
# Este comando é responsável por executar o teste lógico soma==4 
# (o valor de soma é 4?) sobre todas as linhas de soma. Como resultado, 
# gera-se uma Series booleana chamada tem_todas, que possuirá o valor True 
# associado a todas as linhas de soma que possuam o valor 4.
# =============================================================================









