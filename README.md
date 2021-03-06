# Parte 1: Analise_de_Sentimentos
![alt text](https://zenodo.org/badge/302881353.svg)

O código principal em Pytho nse encontra na pasta "/scr", e os métodos extras e treinamento dos classificadores se encontram no caderno Jupyter.

Este repositório apresenta três algoritmos para análise de sentimentos, inicialmente pensado para o português, classificando os sentimentos em:

 - felicidade/alegria;
 - tristeza;
 - raiva.

O banco de dados utilizado é um subconjunto daquele apresentado no artigo https://medium.com/@alegeorgelustosa/an%C3%A1lise-de-sentimentos-em-python-2a7d04a836e0, passado pelo processo de data augmentation através do GPT-2,  transcrito em um arquivo ".csv".

São treinadas e testadas três implementações:

A primeira bem simples, utilizando um classificador SVM com kernel linear e representação vetorial dos textos através do TF-IDF.

A segunda estratégia faz uso de uma rede recorrente baseada na arquitetura LSTM.

E por fim uma estratégia utilizando o Google bert, ferramenta considerada o estado da arte para processamento de linguagem natural junto ao GPT-3 (que infelizmente não tem código aberto igual ao Bert).  O uso do Bert se dá apenas para ilustrar o estado da arte da literatura, uma vez que o banco de dados utilizado é bastante singelo, impossibilitando visualizar o pleno potencial do bert, se tratando de um canhão para matar uma mosca.

O comparativo entre as estratégias pode ser visto tanto nas implementações quanto no artigo do medium (https://medium.com/ds4data/acessibilidade-parte-1-an%C3%A1lise-de-sentimentos-em-textos-fbf6f4de9918) mostrando como utilizar essas ferramentas para análise de textos. Esse artigo faz parte de um artigo de quatro partes com o objetivo de servir como introdução, minha principalmente, a estratégias e métodos voltados a acessibilidade.

As implementações de treinamento fazem uso de Jupyter notebook e do Google Collab, para aumentar a acessibilidade em qualquer dispositivo, e pode ser acessada pelo caderno contidos no repositório, ou através do link: https://colab.research.google.com/drive/1OH-A8_CvvUnmockaxeXVUTuuI-32zGIF?usp=sharing

A pasta /scr contém o melhor algoritmo testado (aquele baseado na arquitetura LSTM) implementado em um script python único, junto com o arquivo de tokenização e o arquivo correspondente aos pesos e configurações do modelo Tensorflow.

 
