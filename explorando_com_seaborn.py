# -*- coding: utf-8 -*-
"""
DataVisualization - Explorando com Seaborn
"""

import pandas as pd
import seaborn as sns

dados = pd.read_csv('tips.csv')


# renomeando colunas;

dados.columns
renomear = {'total_bill' : 'valor_da_conta',
            'tip' : 'gorjeta',
            'dessert' : 'sobremesa',
            'day' : 'dia_da_semana',
            'time' : 'hora_do_dia',
            'size' : 'total_de_pessoas'
    }

gorjetas = dados.rename(columns = renomear)
gorjetas

# traduzindo campos;
gorjetas.sobremesa.unique()
sim_nao = {'No' : 'Não',
           'Yes' : 'Sim'}

gorjetas.sobremesa = gorjetas.sobremesa.map(sim_nao)
gorjetas.head()

gorjetas.dia_da_semana.unique()
dias = {'Sun' : 'Domingo',
        'Sat' : 'Sábado',
        'Thur' : 'Quinta',
        'Fri' : 'Sexta'
        }

gorjetas.dia_da_semana = gorjetas.dia_da_semana.map(dias)
gorjetas.head()

hora = {'Dinner' : 'Jantar',
        'Lunch' : 'Almoço'
        }

gorjetas.hora_do_dia = gorjetas.hora_do_dia.map(hora)
gorjetas.head()

"""ANALIZANDO VALOR DA CONTA E GORJETA"""

sns.scatterplot(x = 'valor_da_conta', y = 'gorjeta', data = gorjetas)
# visualmente o valor da gorjeta aumenta conforme aumenta o valor da conta;

print(f'A base de dados contém {gorjetas.shape[0]} de registros')
# verificando nº de registros;

print(f'Registros não nulos')
gorjetas.count()
# verificando se há registros nulos no DF;

"""CRIANDO UM CAMPO NO DF"""
gorjetas['porcentagem'] = gorjetas['gorjeta'] / gorjetas['valor_da_conta']

gorjetas.porcentagem = gorjetas.porcentagem.round(2)
gorjetas

# visualizando grafico;
porcentagem_conta = sns.scatterplot(x = 'valor_da_conta',
                                    y = 'porcentagem', data = gorjetas)

# visualmente o valor da conta não é proporcional ao valor da gorjeta;

"""UTILIZANDO O RELPLOT"""
porcentagem_conta_linha = sns.relplot(x = 'valor_da_conta',
                                      y = 'porcentagem',
                                      kind = 'line',
                                      data = gorjetas)

"""UTILIZANDO LMPLOT"""
sns.lmplot(x = 'valor_da_conta', y = 'porcentagem', data = gorjetas)

"""ANALIZANDO A COLUNA SOBREMESA"""
gorjetas[gorjetas.sobremesa == 'Sim'].describe()
gorjetas[gorjetas.sobremesa == 'Não'].describe()

sns.catplot(x='sobremesa', y='gorjeta', data = gorjetas)
# gerando gráfico categórico;

sns.relplot(x = 'valor_da_conta', y = 'gorjeta', hue = 'sobremesa',
            data = gorjetas)

sns.relplot(x = 'valor_da_conta', y = 'gorjeta', hue = 'sobremesa',
            col='sobremesa',
            data = gorjetas)

# traçando uma linha no grafico;
sns.lmplot(x='valor_da_conta', y='gorjeta', col='sobremesa', hue='sobremesa',
           data = gorjetas)


sns.lmplot(x='valor_da_conta', y='porcentagem', col='sobremesa',
           hue='sobremesa', data = gorjetas)
# vizualmente existe uma diferença no valor da gorjeta daqueles que pediram
# e aqueles não pediram sobremesa;

sns.relplot(x = 'valor_da_conta', y = 'gorjeta', col='sobremesa',
            hue = 'sobremesa', kind = 'line', data = gorjetas)


"""TESTE DE HIPOTESE"""
from scipy.stats import ranksums
sobremesa = gorjetas.query("sobremesa == 'Sim'").porcentagem
sem_sobremesa = gorjetas.query("sobremesa == 'Não'").porcentagem

r = ranksums(sobremesa, sem_sobremesa)

print(f'O valor do p-value é {r.pvalue.round(2)}')
# a distribuição da gorjeta nos grupos é a mesma;

"""ANALISANDO OS DIAS DA SEMANA"""
# verificando os dias da semana;
gorjetas.dia_da_semana.unique()

# realizando um plot categorico;
sns.catplot(x='dia_da_semana', y='valor_da_conta', data=gorjetas)

sns.relplot(x='valor_da_conta', y='gorjeta', hue='dia_da_semana',
            data=gorjetas)

sns.relplot(x='valor_da_conta', y='gorjeta', hue='dia_da_semana',
            col='dia_da_semana', data=gorjetas)

sns.relplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana',
            col='dia_da_semana', data=gorjetas)

sns.lmplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana',
            col='dia_da_semana', data=gorjetas)


"""REALIZANDO ANALISE DESCRITIVA"""

media_geral_gorjetas = gorjetas.gorjeta.mean()
print(f'A média geral das gorjetas é {media_geral_gorjetas}')

# chamando a media das gorjetas por cada dia;
gorjetas.groupby(['dia_da_semana']).mean()[['valor_da_conta', 'gorjeta',
                                            'porcentagem']]


# verificando a frequencia de cada dia;
freq = gorjetas.dia_da_semana.value_counts()
print(f'Frequencia dos dias: \n{freq}')

"""REALIZANDO TESTE DE HIPOTESE"""

# Hipotese nula (null) -> A distribuição do valor da conta é igual no
# sábado e no domingo;

# Hipotese alternativa (null) -> A distribuição do valor da conta NÃO é igual 
# no sábado e no domingo;

conta_domingo = gorjetas.query("dia_da_semana == 'Domingo'").valor_da_conta
conta_sabado = gorjetas.query("dia_da_semana == 'Sabado'").valor_da_conta

r2 = ranksums(conta_domingo, conta_sabado)
print(f'O valor p-value é {r2.pvalue}')

"""ANALISE DA HORA DO DIA"""
sns.catplot(x='hora_do_dia', y='valor_da_conta', data=gorjetas)
sns.catplot(x='hora_do_dia', y='valor_da_conta', kind='swarm', data=gorjetas)
sns.violinplot(x='hora_do_dia', y='valor_da_conta', data=gorjetas)
sns.boxplot(x='hora_do_dia', y='valor_da_conta', data=gorjetas)

almoco = gorjetas.query("hora_do_dia == 'Almoço'").valor_da_conta
sns.distplot(almoco, kde=False)

jantar = gorjetas.query("hora_do_dia == 'Jantar'").valor_da_conta
sns.distplot(jantar, kde=False)

"""TESTE DE HIPOTESE 2"""
gorjetas.groupby(['hora_do_dia']).mean()[['valor_da_conta', 'gorjeta',
                                          'porcentagem']]

r3 = ranksums(jantar, almoco)
print(f'O valor do p-value é de {r3.pvalue}')
print('A Hipótese é alternativa')

porc_almoco = gorjetas.query("hora_do_dia == 'Almoço'").porcentagem
porc_jantar= gorjetas.query("hora_do_dia == 'Jantar'").porcentagem

r4 = ranksums(porc_almoco, porc_jantar)
print(f'A distribuição % da gorjeta é {r4.pvalue}')
print('Portanto a HIPOTESE é null')




