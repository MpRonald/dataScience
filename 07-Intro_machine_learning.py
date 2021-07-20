# -*- coding: utf-8 -*-
"""
Livro pandas;
Capítulo 7 - Introdução à Machine Learning

"""
"""
Machine Learning é o campo da ciência que se preocupa em investigar como 
computadores podem aprender a executar tarefas baseando-se no uso de dados. 
Os processos de Machine Learning são realizados por programas de computador 
que aprendem a reconhecer padrões complexos e conseguem tomar decisões 
inteligentes através de análise de dados."""

# =============================================================================
# A biblioteca scikit-learn disponibiliza cerca de vinte diferentes medidas 
# de distância para os seus usuários 
# (https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html).
# =============================================================================

# Criando um classificador k-NN
# Avaliando o programa com método LOO

# parte1 -> importando bibliotecas;
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# parte2 -> Carregando a base de dados;
flags = pd.read_csv("flags_transf.csv")

# parte3 -> configurando os parametros e variaveis auxiliares;
# valor de k a ser usado no k-nn
k = 3

# nomes do labels (rotulos de classe)
labels = ['red', 'green', 'blue', 'gold', 'white', 'black', 'orange']
q = len(labels)

# numero de registro da base em treinamento (=194)
N = flags.shape[0]

# parte4 -> criando um classificador com algoritmo k-NN;
# fazendo estimativa de desempenho preditivo com método LOO (leave-one-out)

# laço para percorrer cada rotulo
for j in range(0,q):
    print(25*'-')
    print(f'Processando Rótulos {labels[j]}')

# instaciando uma matriz de confusão com rótulo j;
mc = pd.DataFrame({'predito_nao':[0,0], 'predito_sim':[0,0]},
                  index=['real_nao', 'real_sim'])

# dividindo a base de treinamemnto verticalmente em duas partes:
# X(atributos preditivos) e Y(atributo classe)
X = flags.drop(columns=labels)
Y = flags[labels[j]]

# for i, laço que realiza o LOO para rótulo j;
for i in range(0,N):
    # treino do modelo;
    X_treino = X.drop([i])
    Y_treino = Y.drop([i])

# separando objetos de teste;
X_teste = X.iloc[[i],:]
Y_teste = Y.iloc[i]

# treinando o modelo k-NN com os dados de treino;
modelo = KNeighborsClassifier(n_neighbors = k)
modelo.fit(X_treino, Y_treino)

# testando modelo k-NN com objeto de teste;
pred = modelo.predict(X_teste)

# atualizando a celula adequada da matriz de confusão em função do
# resultado do teste 

if Y_teste == 0:
    if pred==0:mc.iloc[0,0]+=1

if pred==1:mc.iloc[0,1]+=1

else:
    if pred==0:mciloc[1,0]+=1

if pred==0:mciloc[1,1]+=1

# fim do LOO para rotulo;

# imprimindo a sua matriz de confusão e acurácia;
print(mc)
acuracia = (mc.iloc[0,0] + mc.iloc[1,1]) / N
print(f'Acurácia {round(acuracia,2)}')


print(mc)
acuracia = (mc.iloc[0,0] + mc.iloc[1,1]) / N
print('acurácia = ',round(acuracia,2))


# =============================================================================
# =============================================================================
# =============================================================================
# # # ABAIXO CÓDIGO COPIA DIRETAMENTE DO LIVRO, O MESMO DO DE CIMA # # #
# =============================================================================
# =============================================================================
# =============================================================================


import pandas as pd    
 from sklearn.neighbors import KNeighborsClassifier
#--------------------------------------------------------- 
#Parte 2: carrega a base de dados de treinamento 
# para um DataFrame #---------------------------------------------------------
flags = pd.read_csv('c:/bases/flags_transf.csv')
#--------------------------------------------------------- 
#Parte 3:
# configura os parâmetros e variáveis auxiliares  
#--------------------------------------------------------- 
#valor de k a ser usado no k-nn
k=3 #nomes dos labels (rótulos de classe)
labels=['red', 'green', 'blue', 'gold', 'white', 'black', 'orange']
#número de labels (=7)
q = len(labels)  
#número de registros da base de treinamento (=194)
N = flags.shape[0] 
#------------------------------------------------------------ 
#Parte 4: cria um classificador com o algoritmo k-NN  
#         e faz a estimativa do desempenho preditivo  
#         com o método LOO (Leave-One-Out) #------------------------------------------------------------- #------------------------------------------------------------- #4.1 - for j: laço que precorre cada rótulo #------------------------------------------------------------- for j in range(0,q): 
print('------------------------------------------------')
print("PROCESSANDO O RÓTULO ", labels[j])
#--------------------------------------------------------- 
#4.1.1 instancia uma matriz de confusão para o rótulo j 
#---------------------------------------------------------
mc = pd.DataFrame({'predito_nao': [0,0],
'predito_sim':[0,0]},
index = ['real_nao','real_sim'])
#--------------------------------------------------------- 
#4.1.2 divide a base de treinamento verticalmente 
#      em duas partes: X (atributos preditivos) e  
#                      Y (atributo classe) 
#---------------------------------------------------------
X = flags.drop(columns=labels)
Y = flags[labels[j]] 
#--------------------------------------------------------- 
#4.2 - for i: laço que realiza o LOO para o rótulo j 
#--------------------------------------------------------- 
for i in range(0,N):
#----------------------------------------------------- 
#4.2.1 Separa os dados que serão utilizados para  
#      treinar o modelo 
#-----------------------------------------------------
X_treino = X.drop([i])
Y_treino = Y.drop([i])
#----------------------------------------------------- 
#4.2.2 Separa o objeto de teste 
#-----------------------------------------------------
X_teste = X.iloc[[i],:]
Y_teste = Y.iloc[i]
#----------------------------------------------------- 
#4.2.3 Treinamento do modelo k-NN com os dados  
#      de treino 
#-----------------------------------------------------
modelo=KNeighborsClassifier(n_neighbors=k) 
modelo.fit(X_treino,Y_treino)
#----------------------------------------------------- 
#4.2.4 Teste do modelo k-NN com o objeto de teste 
#-----------------------------------------------------
pred = modelo.predict(X_teste) 
#----------------------------------------------------- 
#4.2.5 Atualiza a célula adequada da matriz de  
#      confusão em função do resultado do teste 
#----------------------------------------------------- 
if (Y_teste == 0):
    if (pred == 0): mc.iloc[0,0]+=1 
if (pred == 1): mc.iloc[0,1]+=1 
else:
    if (pred == 0): mc.iloc[1,0]+=1 
if (pred == 1): mc.iloc[1,1]+=1 
#--------------------------------------------------------- 
#4.3 - Fim do LOO para o rótulo j:  
    #      imprime a sua matriz de confusão e acurácia 
    #---------------------------------------------------------
print(mc)
acuracia = (mc.iloc[0,0] + mc.iloc[1,1]) / N
print('acurácia = ',round(acuracia,2))


"""EXPLICAÇÃO CÓDIGO ACIMA"""
"""PARTE I"""
# =============================================================================
# # Em nosso programa, a pandas foi utilizada para executar diversas funções. 
# # A mais importante delas é estruturar a base de dados de treinamento em um 
# # DataFrame. Além disso, nós a utilizamos em diversas operações de fatiamento 
# # (por exemplo, para separar os conjuntos de atributos X e Y) e também para 
# # implementar a matriz de confusão mc. Isso demonstra o quanto a pandas é 
# # importante para a ciência de dados!
# =============================================================================

# =============================================================================
# # Depois de importar a pandas, também fizemos a importação da scikit-learn. 
# # Para utilizar o k-NN oferecido por esta biblioteca, o comando import foi 
# # definido da seguinte forma: from sklearn.neighbors import KNeighborsClassifier
# # Este comando faz a importação da classe KNeighborsClassifier, que faz 
# # parte do módulo neighbors da scikit-learn. É esta a classe que contém a 
# # implementação do algoritmo k-NN na scikit-learn.
# =============================================================================

"""PARTE II"""
# =============================================================================
# # Importação da base de daos para treinamento
# # Esta parte do programa é composta por apenas uma linha, onde importamos 
# # a base de dados de treinamento flags_transf.csv para um DataFrame pandas 
# # denominado flags. Trata-se de uma operação simples, porém necessária em 
# # qualquer programa que envolva a construção de um classificador. Afinal 
# # de contas, para que seja possível construir um classificador, um dos 
# # artefatos necessários é exatamente uma base de dados de treinamento 
# # (o outro é o algoritmo de classificação).
# =============================================================================

"""PARTE III"""
# =============================================================================
# Configuração de parametros
# Neste trecho de código, definimos quatro variáveis para armazenar infomações
# utilizadas durante o processo de construção do classificador:
#     -> k: valor do número de vizinhos a ser adotado pelo k-NN;
#     -> labels: lista que armazena os nomes dos atributos do conjunto Y
#     (rótulo de classe);
#     -> q: o número de rótulos de classe (nesse caso, igual a 7);
#     -> N: o total de objetos da base de treinamento
#     (como sabemos, flags_tranf.csv possui dados de 194 países);
# =============================================================================
    
"""PARTE IV"""
# =============================================================================
# Esta é a parte principal do programa, onde utilizamos o k-NN e o LOO para,
# respectivamente, criar e avaliar classificadores para cada um dos rótulos
# de classe;
# Este processo é implementado através de dois laços for:
#     -> for j in range(0,q): laço externo utilizado para processar cada
#     rótulo de classe (red, green, blue, gold, white, black e orange);
#     -> for i in range(0,N): laço interno responsável pela implementação
#     da avalização LOO;
# Sendo assim, tudo começa no passo 4.1, onde definimos o laço 
# for j in range(0,q): para percorrer toda a lista de rótulos de classe,
# desde red (1º rótulo), até orange(últmo rótulo). Ou seja, este laço
# realizará 7 iterações;
# 
# =============================================================================


# mc = pd.DataFrame({'predito_nao': [0,0],
# 'predito_sim':[0,0]},
# index = ['real_nao','real_sim'])

# =============================================================================
# O comando acima cria uma matriz de confusão mc para rótulo j
# (rótulo concorrente processado). Ao final do processo LOO, a matriz
# estará totalmente preenchida com os resultados completos do teste do rótulo j.
# 
# =============================================================================

# X = flags.drop(columns=labels)
# Y = flags[labels[j]]

# =============================================================================
# No código acima estamos utilzando toda flexibilidade oferecida pela
# funcionalidade de fatiamento de pandas para dividir verticalmente o DF flags
# (que é nossa base de treinamento) em duas partes => X e Y. A fatia X recebe 
# o conjunto de atributos preditivos , ou seja , todos os atributos de flags 
# , exceto os 7 rótulos de classe . Já a fatia Y recebe uma única coluna 
# , correspondente ao rótulo de classe j ( rótulo que está sendo 
# correntemente processado no laço for j ) . Logo depois , o passo 4.2 é 
# iniciado , onde definimos o laço for i in range ( 0 , N ) : 
# para percorrer todos os objetos de treinamento ( que acabaram de ser 
# divididos em X e Y ) e executar o processo de LOO . Esse laço realizará 
# N iterações . A cada iteração , um modelo de classificação será construído 
# utilizando - se N - 1 objetos ( todos , menos o objeto da posição i ) e 
# testado utilizando um único objeto ( o objeto da posição i ) . 
# Vamos agora examinar detalhadamente os trechos de código subordinados 
# ao laço for i . Novamente , nós primeiro reproduzimos o trecho de 
# código e depois apresentamos uma explicação 
# =============================================================================

# =============================================================================
# # 4.2.1 Separa os dados que serão utilizados para # treinar o modelo
# X_treino = X.drop ( [ i ] ) Y_treino = Y.drop ( [ i ] ) Nesta parte , 
# realizamos o fatiamento dos DataFrames X e Y com o intuito de separar os 
# objetos que serão utilizados para treinar o modelo . Conforme acabamos de 
# comentar , a cada passo do LOO todos os objetos são utilizados para treinar 
# o modelo , exceto um único objeto i .
# =============================================================================

"""Novamente , nós primeiro reproduzimos o trecho de código e depois 
apresentamos uma explicação . """

# =============================================================================
# # 4.2.1 Separa os dados que serão utilizados para # treinar o modelo 
# X_treino = X.drop ( [ i ] ) Y_treino = Y.drop ( [ i ] ) Nesta parte , 
# realizamos o fatiamento dos DataFrames X e Y com o intuito de separar 
# os objetos que serão utilizados para treinar o modelo . Conforme acabamos 
# de comentar , a cada passo do LOO todos os objetos são utilizados para 
# treinar o modelo , exceto um único objeto i .
# =============================================================================
 
# 4.2.2 Separa o objeto de teste 
# =============================================================================
# X_teste = X.iloc [ [ i ] , : ] Y_teste = Y.iloc [ i ] E aqui separamos o 
# objeto que será utilizado para teste na iteração corrente do LOO 
# ( objeto da posição i na base de dados ) . Veja que pegamos tanto a 
# parte X do objeto ( atributos preditivos ) como a sua parte
# Y ( sua classe real ) . Precisamos da classe real para compará - la 
# com a classe que será predita pelo modelo de classificação e , assim , 
# realizar a atualização da matriz de confusão ( passo 4.2.5 do programa ) . 
# É importante observar que a sintaxe X.iloc [ [ i ] , : ] foi utilizada 
# para forçar o tipo de X_teste como um DataFrame . Se não tivéssemos feito 
# isso , o fatiamento retornaria uma Series por default , já que resulta 
# em apenas uma linha ( se estiver em dúvida , reveja o tópico sobre 
#                      fatiamento do capítulo 3 ) . 
# =============================================================================

# =============================================================================
# # 4.2.3 Treinamento do modelo k - NN com os dados 
# # de treino modelo = KNeighborsClassifier ( n_neighbors = k ) 
# modelo.fit ( X_treino , Y_treino ) Esta é a parte mais importante de todo 
# o programa , onde criamos o modelo de classificação . Apesar disso , veja 
# como ela é incrivelmente simples , consistindo apenas em duas linhas de 
# código . Inicialmente , instanciamos um objeto chamado modelo , do tipo 
# kNeighborsClassifier . É importante chamar a atenção para dois aspectos .
# O primeiro é que , para utilizar a classe kNeighborsClassifier , 
# torna - se preciso preliminarmente fazer o import da respectiva classe 
# no scikit - learn , algo que fizemos logo no início de nosso programa 
# ( se você for utilizar outro algoritmo de classificação , como o 
# Naïve Bayes , deverá fazer a importação da classe adequada ) . 
# O segundo aspecto importante é que o kNeighborsClassifier foi 
# instanciado com o parâmetro n_neighbors = k .
# Este parâmetro é utilizar para especificar o número de vizinhos 
# a ser adotado pelo k - NN . Desta forma , estamos definindo 3 vizinhos , 
# já que havíamos feito a atribuição k = 3 na parte 2 do programa . 
# =============================================================================

# =============================================================================
# Após instanciarmos o objeto do tipo kNeighborsClassifier com o parâmetro 
# adequado , podemos utilizá - lo para efetivamente treinar o modelo de 
# classificação . Para isto , basta fazer uma chamada para o método fit ( ) , 
# passando como parâmetros as partes X e Y da base de treinamento , que 
# neste caso estão respectivamente estruturadas nos DataFrames X_treino 
# e Y_treino . A classe kNeighborsClassifier aceita outros parâmetros além 
# de n_neighbors . Um parâmetro muito importante , por exemplo , é metrics , 
# que serve para definir a medida de distância a ser empregada . 
# 
# Para informações completas , consulte a documentação de kNeighborsClassifier 
# em https : / / scikit - learn.org / stable / modules / generated / sklearn.neighbors.KNeighborsClassifier.html . 
# =============================================================================

# 4.2.4 Teste do modelo k - NN com o objeto de teste  
# =============================================================================
# pred = modelo.predict ( X_teste ) Uma vez o modelo tendo sido criado , 
# podemos utilizá - lo para classificar o nosso objeto de teste i . 
# Isso é feito com o uso do método predict ( ) . Como parâmetro , devemos 
# passar as características ( features ) de i , isto é , a sua parte X . 
# Em nosso programa , essas características estão armazenadas no 
# DataFrame X_teste . Como resultado , predict ( ) vai retornar um valor 
# binário : 0 : significa que o objeto de teste i não está associado à 
# classe j . 
# =============================================================================

# =============================================================================
# Isto é , o modelo considera que a cor j não está presente na bandeira do 
# país i . 1 : significa que o objeto de teste i está sim , 
# associado à classe j . Ou seja , para o modelo de classificação , 
# a cor j está presente na bandeira do país i . Veja que , em nosso programa 
# o valor retornado é armazenado em uma variável chamada pred . 
# =============================================================================

# =============================================================================
# # 4.2.5 Atualiza a célula adequada da matriz de 
# # confusão em função do resultado do teste
# if ( Y_teste = = 0 ): 
#     if ( pred = = 0 ):mc.iloc [ 0,0 ] + = 1 
# if ( pred = = 1 ) : mc.iloc [ 0,1 ] + = 1 
# else: 
#     if ( pred = = 0 ) : mc.iloc [ 1,0 ] + = 1 
# if ( pred = = 1 ) : mc.iloc [ 1,1 ] + = 1 
# Este é o último trecho de código subordinado ao laço for i . 
# 
# Nele , comparamos o valor predito pelo modelo de classificação ( pred )
# com o valor real do rótulo de classe na base de dados de treinamento 
# ( Y_teste ) . Assim , poderemos descobrir se o teste resultou em um 
# VP , FP , FN ou VN , atualizando a célula adequada da matriz de 
# confusão mc . 
# =============================================================================

# =============================================================================
# # 4.3 - Fim do LOO para o rótulo j : # imprime a sua matriz de confusão e 
# acurácia 
# print (mc) acuracia = (mc.iloc[0,0] + mc.iloc[1,1]) / N
# print ('acurácia = ',round(acuracia,2))
# Chegamos aos três comandos finais de nosso programa ( passo 4.3 ).
# Esses comandos são executados para cada rótulo de classe j , depois que 
# os N modelos de classificação foram gerados e testados no processo de LOO .
# Nesse momento , a matriz de confusão do label j estará prontinha . 
# Então , imprimimos essa matriz e também calculamos e imprimimos o 
# valor da acurácia do modelo de classificação . Análise dos resultados 
# =============================================================================

# =============================================================================
# A base de dados flags_transf.csv possui um número muito pequeno de objetos , 
# algo que não favorece o processo de construção do classificador 
# ( o algoritmo k - NN fica com pouca informação para aprender a mapear X em Y ) 
# =============================================================================

# =============================================================================
# Apesar disso , podemos considerar que a estimativa do desempenho 
# preditivo — computada pelo processo de LOO — revelou que o modelo k - NN 
# conseguiu atingir uma performance surpreendentemente boa para alguns dos 
# rótulos de classe . Essa conclusão pôde ser obtida levando - se em conta 
# não apenas o valor da acurácia de cada rótulo , mas principalmente através 
# da observação da composição da matriz de confusão . Neste sentido , podemos 
# considerar , por exemplo , que o desempenho preditivo do classificador 
# para o rótulo green foi o melhor dentre todos os labels . 
# =============================================================================

# =============================================================================
# A matriz de confusão resultante do teste LOO deste rótulo é reproduzida a 
# seguir : 
#     PROCESSANDO O RÓTULO 
# green predito_nao predito_sim real_nao 88 15 real_sim 17 74 acurácia = 0.84 
# Veja que a matriz de confusão está bastante equilibrada . Isso significa 
# que o classificador do rótulo green conseguiu se sair bem tanto para 
# a previsão do valor " não " , como do valor " sim " . No geral , o 
# classificador quase não errou , pois foram poucos casos de FP e FN em 
# relação ao número total de casos . Em outras palavras , o valor de VN é 
# bem maior do que o de FP e o valor de VP é bem maior do que o de FN . 
# A acurácia total foi de 84 % . Por outro lado , podemos considerar que 
# o classificador que apresentou o pior desempenho preditivo foi o do 
# rótulo orange , cuja matriz de confusão é apresentada a seguir : 
# PROCESSANDO O RÓTULO orange predito_nao predito_sim real_nao 163 5 
# real_sim 20 6 acurácia = 0.87 
# =============================================================================

# =============================================================================
# Curiosamente , o valor de acurácia do classificador para o rótulo orange 
# é maior do que o obtido para o rótulo green . No entanto , esse resultado 
# é ilusório . Ao observar a matriz , é trivial perceber que o classificador 
# teve uma boa taxa de acertos para o valor " não " , ( seu valor de VN é 
# bem maior do que o de FP ) , mas errou quase todas as previsões para 
# o valor " sim " ( tem valor de FN bem maior do que de VP ) . 
# =============================================================================

# =============================================================================
# A matriz de confusão está bastante desequilibrada e isso não é bom ! 
# Na verdade , seu valor alto de Acurácia ( 87 % ) , foi determinado 
# unicamente pelo fato de a base utilizada ter muito mais objetos " não " 
# ( onde o classificador se sai bem ) do que " sim " ( onde o desempenho do 
# classificador é insatisfatório ) . De fato , qualquer algoritmo de 
# classificação teria dificuldades para conseguir um bom desempenho ao 
# classificar o rótulo orange , pois há muito poucas bandeiras que possuem 
# essa cor na base de treinamento ( apenas 26 dentre os 194 países ) . 
# =============================================================================

# =============================================================================
# O modelo de classificação não teve informação suficiente para aprender 
# as características de um país que possui a cor laranja em sua bandeira . 
# Sugerimos ao leitor examinar as demais matrizes de confusão , empregando 
# o mesmo método de análise para determinar quais classificadores apresentaram 
# um bom desempenho preditivo . Conforme mencionado anteriormente , só faz 
# sentido colocar um classificador em produção se a estimativa obtida para a 
# sua acurácia for satisfatória . Sobre esse assunto , duas observações 
# importantes precisam ser realizadas : A definição de acurácia alta ou 
# satisfatória varia de acordo com o tipo de problema e o nível de 
# exigência da empresa que vai utilizar o classificador . Na prática , 
# muitas vezes a primeira rodada de um processo de ciência de dados não é 
# suficiente para produzir um modelo satisfatório para a empresa . 
# =============================================================================

# =============================================================================
# Neste caso , será preciso refazer alguma das etapas do projeto . Por exemplo , 
# realizar novas transformações sobre a base de dados ; ou tentar obter 
# arquivos externos para combinar com a base , enriquecendo assim o conjunto de 
# informações a serem disponibilizadas para o algoritmo de classificação . 
# =============================================================================

# =============================================================================
# A ciência de dados é , por natureza , um processo cíclico , que usualmente 
# necessita de algumas iterações até que o melhor resultado seja obtido . 
# =============================================================================
# =============================================================================
# CLASSIFICAÇÃO MULTIRRÓTULO 
# Classificação multirrótulo é um tema extremamente rico , que nos últimos 
# anos vem sendo bastante estudado na Ciência da Computação . Se você gostou 
# do assunto e deseja aprender um pouco mais , uma dica é consultar o tutorial 
# disponibilizado em https : / / doi.org / 10.5753 / sbc . 7.3 . 
# =============================================================================

# =============================================================================
# Conclusões e comentários finais E assim , chegamos ao fim de nosso livro , 
# onde foram apresentados os conceitos fundamentais e as principais técnicas 
# para Data Wrangling oferecidas pela biblioteca pandas , a mais importante 
# biblioteca para ciência de dados do Python . A pandas oferece ao usuário 
# técnicas provenientes de diferentes áreas ( Estatística , Computação etc . ) 
# com o intuito de viabilizar o processo de seleção , estudo , limpeza e 
# transformação de bases de dados estruturadas nos mais diversos formatos . 
# =============================================================================

# =============================================================================
# Ela é incrivelmente flexível e poderosa , o que explica a sua larga 
# utilização por profissionais envolvidos com ciência de dados em todo o
# mundo .
# =============================================================================











































































































































