# Proyecto Final UDD - Juan Camilo Rivera G — API de Análisis de Sentimientos (Reviews Google)

Esta API permite predecir el **sentimiento** (Negativo, Neutral, Positivo) y calcular la **subjetividad** de un review de google usando modelos entrenados con Word2Vec y XGBoost.

---

## ¿Cómo funciona?

- La API está desarrollada en **Flask** y desplegada en Render.
- Usa un modelo de Word2Vec para vectorizar el texto y un modelo XGBoost para predecir el sentimiento.

---
## 🛠 Archivos importantes

- `app.py`: lógica principal Flask.
- `requirements.txt`: dependencias.
- `download_models.sh`: descarga modelos grandes desde Google Drive.
- `runtime.txt`: versión específica de Python (3.10.11).

## ⚙️ Endpoints

### `POST /predict`

**Descripción:**  
Recibe un texto y devuelve la predicción del sentimiento y la subjetividad.

**Request body (JSON):**

```json
{
  "text": "No recipe book Unable recipe book"
}
