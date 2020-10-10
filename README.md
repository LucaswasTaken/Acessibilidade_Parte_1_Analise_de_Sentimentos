# Bert Analise_de_Sentimentos
Este repositório apresenta dois algoritmos para análise de sentimentos em textos em qualquer linguagem (inicialmente pensado para o português), classificando os sentimentos em:

 - felicidade;
 - tristeza;
 - raiva.

São apresentadas duas implementações. 

Uma utilizando o Google bert, ferramenta considerada o estado da arte para processamento de linguagem natural junto ao GPT-3 (que infelizmente não tem código aberto igual ao Bert). 

A segunda estratégia faz uso de uma rede recorrente baseada na arquitetura LSTM. A rede é bem mais simples, porém o problema a se tratar também é simples. O uso do Bert se dá apenas para ilustrar o estado da arte da literatura.

As implementações fazem uso de Jupyter notebooks e do Google Collab, para aumentar a acessibilidade em qualquer dispositivo, e pode ser acessada pelos cadernos contidos no repositório, ou através do link: https://colab.research.google.com/drive/1OH-A8_CvvUnmockaxeXVUTuuI-32zGIF?usp=sharing 

O banco de dados utilizado é um subconjunto daquele apresentado no artigo https://medium.com/@alegeorgelustosa/an%C3%A1lise-de-sentimentos-em-python-2a7d04a836e0, transcrito em um arquivo ".csv". 
