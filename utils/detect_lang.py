import pickle

# Load a variable from a file using pickle
def load_variable(filepath):
    with open(filepath, 'rb') as file:
        variable = pickle.load(file)
    return variable


def predict_language(sentence, vectorizer, model):
    # Preprocess the sentence
#     preprocessed_sentence = preprocess(sentence)  # Replace `preprocess` with your own preprocessing function

    # Convert the preprocessed sentence into numerical features
    features = vectorizer.transform([sentence])

    # Make the prediction using the language detection model
    predicted_label = model.predict(features)[0]

    return predicted_label