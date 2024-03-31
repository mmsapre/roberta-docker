from transformers import AutoTokenizer, AutoModelForSeq2SeqLM ,AutoModelForSequenceClassification
import os

def download_model(model_path, model_name):
     if not os.path.exists(model_path):
        os.makedirs(model_path)

     tokenizer = AutoTokenizer.from_pretrained(model_name)
     model = AutoModelForSequenceClassification.from_pretrained(model_name)
     model.save_pretrained(model_path)
     tokenizer.save_pretrained(model_path)
download_model('models/tinyroberta-squad2/', 'deepset/tinyroberta-squad2')    
#download_model('models/bert-base-ner/', 'dslim/bert-base-NER')    
