from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM ,AutoModelForSequenceClassification ,AutoModelForTokenClassification
from transformers import pipeline

def get_model(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    return model, tokenizer

model_loaded_from_local = AutoModelForSequenceClassification.from_pretrained('models/tinyroberta-squad2/')
tokenizer_loaded_from_local  = AutoTokenizer.from_pretrained('models/tinyroberta-squad2/')
#tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
#model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
app = Flask(__name__)


@app.route('/load/models/', methods=['GET'])
def translate_endpoint():
        return jsonify({'sucess': 'LoadModel'}), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)