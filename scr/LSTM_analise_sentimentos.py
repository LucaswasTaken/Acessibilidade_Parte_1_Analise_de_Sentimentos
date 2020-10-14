import re
import string
from unidecode import unidecode
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
from  tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

#Definição da classe que realiza a previsão
class Prediction():
    #construtor
    def __init__(self,tokenizer,max_len):
        self.model = None
    #leitura do modelo treinado(google colab)
    def load_model(self):
        self.model = load_model("class_prediction_model.h5")
    #pad-sequencias e previsão    
    def predict_words(self,encoded_data):
        encoded_data = pad_sequences(encoded_data,maxlen = 11 ,padding='pre')
        y_preds = self.model.predict(encoded_data)
        return y_preds

#Leitura do texto a ser avaliado
text = input('digite o texto a ser avaliado: ')

#preprocessamento e limpeza do texto para remover informações espurias
text = unidecode(text.lower())
text= re.sub(r'\[[0-9]*\]', ' ', text)
text = re.sub(r'\s+', ' ', text)
text = re.sub('[^a-zA-Z]', ' ', text )
text = re.sub(r'\s+', ' ', text)  
text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
clean_text = [text]

#tokenização do texto com base no dicionário de treino da rede
with open('tokenizer.pickle', 'rb') as handle:
  tokenizer = pickle.load(handle)

encoded_data = tokenizer.texts_to_sequences(clean_text)

#inicialização da classe de previsão
max_length = 11
pred = Prediction(tokenizer, max_length)    
pred.load_model()

#previsão e determinação do sentimento
y_pred = pred.predict_words(encoded_data)
if(np.argmax(y_pred)==0):
  y_pred_class='raiva'
elif(np.argmax(y_pred)==1):
  y_pred_class='tristeza'
else:
  y_pred_class='alegria'
#impressaço na tela
print('O sentimento é: ', y_pred_class)
