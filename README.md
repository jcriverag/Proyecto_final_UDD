# Proyecto Final UDD - Juan Camilo Rivera G — API de Análisis de Sentimientos (Reviews Google)

Esta API permite predecir el **sentimiento** (Negativo, Neutral, Positivo) y calcular la **subjetividad** de un review de Google usando modelos entrenados con Word2Vec y XGBoost.

---

## 🚀 ¿Cómo funciona?

- La API está desarrollada en **Flask** y desplegada en Render.
- Usa un modelo **Word2Vec** para vectorizar el texto y un modelo **XGBoost** para predecir el sentimiento.
- Además, utiliza **TextBlob** para calcular la subjetividad del texto.

---

## 🗂 Archivos importantes

- `app.py`: lógica principal de Flask (contiene los endpoints y la carga de modelos).
- `requirements.txt`: lista de dependencias necesarias para correr la API.
- `runtime.txt`: versión específica de Python utilizada (3.10.11).
- `google_reviews_model.pkl`: modelo entrenado de clasificación.
- `word2vec_model.model`: modelo Word2Vec entrenado.
- `Proyecto Final UDD - Juan Camilo Rivera G - Reviews google`: Presentación con storytelling del modelo implementado.

---

## ⚙️ Endpoints API:
https://proyecto-final-udd.onrender.com/predict

### `POST /predict`

**Descripción:**  
Recibe un texto y devuelve la predicción del sentimiento y la subjetividad.

**Ejemplo Request body (JSON):**

```json
{
  "text": "Ten best food promote good health Good health essential long healthy lifestyle make habit eat foods promote good health. Eat fruits veggies every day."
}
