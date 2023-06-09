# Language Detection and Translation Flask API

This is a Flask API project for language detection and translation between Arabic and English.

## Project Overview

The project provides a web interface where users can input a sentence and get it translated between Arabic and English based on the detected language. The API utilizes the langdetect library for language detection and the Hugging Face Transformers library for translation.

## Prerequisites

- Python 
- Flask 
- langdetect 
- Transformers 



### Create Virtual Evironment :

```
python -m venv <env_name>
<env_name>\Scripts\activate
```

```
pip install -r requirements.txt
```

### Run the server :
```
python API.py
```
### from browser visit :  
```
http://127.0.0.1:5000
```