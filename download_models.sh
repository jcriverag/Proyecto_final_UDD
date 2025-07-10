#!/bin/bash

echo "Descargando modelos desde Google Drive..."

# Descargar google_reviews_model.pkl
gdown --id 16uThj2hX8NEAcLL9-8YTQxGeTsmqtWuj -O google_reviews_model.pkl

# Descargar word2vec_model.model
gdown --id 1uTkEIc8yyA1bpFitRtNOYXsTfyT3knR_ -O word2vec_model.model

echo "¡Descarga completa! ✅"
