# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:26:07 2020

Capitulo 2 - Estrutura de Dados Series
"""

import pandas as pd

# criando a Series;
notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])

# criando Series alunos;
lst_matriculas = ['M02','M05','M13','M14','M19']
lst_nomes = ['Bob','Dayse','Bill','Cris','Jimi']

alunos = pd.Series(lst_matriculas, index=lst_nomes)
print(alunos)

# o metodo index é o contrutor uma lista de indice;

# criando Series à partir de um dict
dic_alunos = {'M02':'Bob','M05':'Dayse','M13':'Bill',
 'M14':'Cris','M19':'Jimi'}

alunos = pd.Series(dic_alunos)
print(alunos)

# Propiedades básicas das series;

import pandas as pd
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
 'M14':'Cris','M19':'Jimi'})

# atribuindo nome p/ vetores de dados e rótulos;
alunos.name = 'alunos'
alunos.index.name = 'matrículas'


# name e index.name renomeiam os rótulos (labels)
tamanho = alunos.size                  
dados   = alunos.values                
rotulos = alunos.index                 
alunos_tipo = type(alunos)             
alunos_dtype = alunos.dtype            
alunos_idx_dtype = alunos.index.dtype

print('número de elementos: ', tamanho)
print('vetor de dados: ', dados)
print('vetor de rótulos: ', rotulos)
print('tipo (type): ', alunos_tipo)
print('dtype da Series:', alunos_dtype)
print('dtype do vetor de rótulos:', alunos_idx_dtype)


# indexação booleana;
import pandas as pd
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
 'M14':'Cris','M19':'Jimi'})

idx_aprovados = notas[notas >= 7].index
print(alunos[idx_aprovados])

# fazendo uma busca em uma Series;
tem_M13 = 'M13' in alunos
tem_M99 = 'M99' in alunos
print(f'Existe o rótulo M13: {tem_M13}')
print(f'Existe o rótulo M13: {tem_M99}')

# verificando se valor existe na Series;
tem_Bob = alunos.isin(['Bob'])
print(f'Existe Bob: {tem_Bob}')

# inserindo, alterando e removendo elementos de Series;
print(f'Serie Original \n{alunos}')

# inserindo novo aluno;
alunos['M55'] = 'Rakesh'

# alterando nomes;
alunos[['M13', 'M14', 'M19']] = ['Billy', 'Cristy', 'Jimmy']
print(f'Nova Series: \n{alunos}')

# removendo elementos;
alunos = alunos.drop('M02')
print(f'Series Modificada: \n{alunos}')

# modificando indices;
alunos.index = ['M91','M92','M93','M94','M95']
print(alunos)

# usando vetorização com for;
for aluno in alunos: print(aluno) # itera sobre dados;
for indice in alunos.index: print(indice) # itera sobre indices;

import numpy as np

# criando Series s1 e s2;
s1 = pd.Series([2, 4, 6])
s2 = pd.Series([1, 3, 5])
print(s1 * s2)
print(s1 * 2)
print(2 * s2)
print(np.sqrt(s1))
print(np.sqrt(s2))


# o valor NaN (valores nulos ou ausentes)
verde = pd.Series({'BR':1, 'FR': 0, 'IT':1, 'UK': 0})
azul = pd.Series({'AR':1, 'BR':1, 'FR': 1, 'IT':0, 'UK': 1})

soma = verde + azul
print(soma)
print('isnull(soma):')
print(pd.isnull(soma))
# isnull() -> recebe entrada da Series, tem como saida uma
# outra Series com dtype bool;

# indices datetime;
# criando uma Series temporal;
dias = ['10/02/2019', '11/02/2019','12/02/2019','13/02/2019',
 '14/02/2019','15/02/2019']
temp_max = [31,35,34,28,27,27]
serie_temporal = pd.Series(temp_max, index = dias)

# convertendo indice para datetime;
serie_temporal.index = pd.to_datetime(serie_temporal.index,
                                      format='%d/%m/%Y')
print(serie_temporal)


# indexação hierarquica;
moedas  = ['Peso', 'Real', 'Euro', 'Euro', 'Libra']
paises = [['América','América','Europa','Europa','Europa'],
 ['AR','BR','FR','IT','UK']]

paises = pd.Series(moedas, index = paises)
print(paises)
print(paises['América'])


















