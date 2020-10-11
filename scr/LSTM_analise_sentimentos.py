import re
import string
from unidecode import unidecode
from tensorflow.keras.models import load_model
import pickle
import numpy as np

class Prediction():
    def __init__(self,tokenizer,max_len):
        self.model = None
        self.tokenizer = tokenizer
        self.idx2word = {v:k for k,v in self.tokenizer.word_index.items()}
        self.max_length = max_len+1
    
    def load_model(self):
        self.model = load_model("class_prediction_model.h5")
        
    def predict_words(self,encoded_data):
        y_preds = self.model.predict(encoded_data)
        return y_preds

text = input('digite o texto a ser avaliado: ')
text = unidecode(text.lower())
text= re.sub(r'\[[0-9]*\]', ' ', text)
text = re.sub(r'\s+', ' ', text)
text = re.sub('[^a-zA-Z]', ' ', text )
text = re.sub(r'\s+', ' ', text)  
text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
clean_text = [text]

with open('tokenizer.pickle', 'rb') as handle:
  tokenizer = pickle.load(handle)

encoded_data = tokenizer.texts_to_sequences(clean_text)

print(encoded_data)

max_length = 11

pred = Prediction(tokenizer, max_length)    
pred.load_model()

y_pred = pred.predict_words(encoded_data)
if(np.argmax(y_pred)==0):
  y_pred_class='raiva'
elif(np.argmax(y_pred)==1):
  y_pred_class='tristeza'
else:
  y_pred_class='alegria'
print(y_pred_class)