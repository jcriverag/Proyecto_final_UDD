# Proyecto Final UDD — API de Análisis de Sentimientos

Esta API permite predecir el **sentimiento** (Negativo, Neutral, Positivo) y calcular la **subjetividad** de un review de google usando modelos entrenados con Word2Vec y XGBoost.

---

## ¿Cómo funciona?

- La API está desarrollada en **Flask** y desplegada en Render.
- Usa un modelo de Word2Vec para vectorizar el texto y un modelo XGBoost para predecir el sentimiento.

---

## ⚙️ Endpoints

### `POST /predict`

**Descripción:**  
Recibe un texto y devuelve la predicción del sentimiento y la subjetividad.

**Request body (JSON):**

```json
{
  "text": "No recipe book Unable recipe book"
}
