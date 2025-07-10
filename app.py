from flask import Flask, request, jsonify
import joblib
import numpy as np
import re
from gensim.models import Word2Vec
from textblob import TextBlob

# Cargar modelos
xgb_model = joblib.load('google_reviews_model.pkl')
w2v_model = Word2Vec.load('word2vec_model.model')

# Obtener tamaño de vector
vector_size = w2v_model.vector_size

# Función de limpieza simple
def limpiar_texto(desc):
    desc = desc.lower()
    desc = re.sub('[^a-zA-Z]', ' ', desc)
    desc = re.sub(r'\s+', ' ', desc).strip()
    return desc

# Función de vector promedio
def vector_promedio(tokens, model, vector_size):
    vectores = [model.wv[word] for word in tokens if word in model.wv]
    if len(vectores) > 0:
        return np.mean(vectores, axis=0)
    else:
        return np.zeros(vector_size)

# Crear app Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    text = data.get('text')

    if text is None:
        return jsonify({'error': 'Debes enviar "text" en el JSON'}), 400

    # Limpiar texto
    cleaned_text = limpiar_texto(text)
    tokens = cleaned_text.split()

    # Calcular subjectivity
    subjectivity = TextBlob(text).sentiment.subjectivity

    # Vector promedio Word2Vec
    vector = vector_promedio(tokens, w2v_model, vector_size)

    # Concatenar subjectivity
    final_vector = np.concatenate((vector, np.array([subjectivity]))).reshape(1, -1)

    # Predecir
    prediction = xgb_model.predict(final_vector)[0]

    # Mapear predicción a texto
    sentiment_map = {0: 'Negativo', 1: 'Neutral', 2: 'Positivo'}
    result = sentiment_map.get(prediction, "Desconocido")

    return jsonify({
        'prediction': int(prediction),
        'sentiment': result,
        'subjectivity': subjectivity
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
