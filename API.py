from flask import Flask, request, jsonify,render_template
from transformers import MarianTokenizer, MarianMTModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from utils import detect_lang,translation

from langdetect import detect
import unicodedata



app = Flask(__name__)

lang_model_path = r'models\lang_model.pkl'
lang_vectorizer_path = r'models\lang_vectorizer.pkl'

lang_model = detect_lang.load_variable(lang_model_path)
lang_vectorizer = detect_lang.load_variable(lang_vectorizer_path)


ar_en_model_path = model_path = r'models\ar-en-model'
en_ar_model_path = model_path = r'models\en-ar-model'

# Load the tokenizer and model
ar_en_model = AutoModelForSeq2SeqLM.from_pretrained(ar_en_model_path)
ar_en_tokenizer = AutoTokenizer.from_pretrained(ar_en_model_path)

en_ar_model = AutoModelForSeq2SeqLM.from_pretrained(en_ar_model_path)
en_ar_tokenizer = AutoTokenizer.from_pretrained(en_ar_model_path)


def check_for_language_chars(sentence):
    for char in sentence:
        category = unicodedata.category(char)
        if category.startswith('L'):  # 'L' category represents letters
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    print(request.form)
    sentence = request.form['text']
    word_exist = check_for_language_chars(sentence)
    if word_exist:
        lang = detect(sentence)
        
        if lang == "ar":
            lang = "Arabic"
            translated_text = translation.translate(sentence, ar_en_model, ar_en_tokenizer)
        elif lang == "en":
            lang = "English"
            translated_text = translation.translate(sentence, en_ar_model, en_ar_tokenizer)
        else:
            lang = "Other"
            translated_text = "Not-Support"
            
    else:
        return "Please Enter Valid Sentence"

    # return jsonify({'translation': translated_text})
    print(translated_text)
    return  "Input Sentence is :>>> " + sentence+ "\nLanguage is :>>>>  "  + lang + " \n And translation is :>>>>" + str(translated_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
