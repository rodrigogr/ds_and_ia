from pydantic import BaseModel
from fastapi import FastAPI
import joblib
import uvicorn

# Instância do FastAPI
app = FastAPI()

# Classe que terá od dados do request body para API
class request_body(BaseModel):
    horas_estudo: float

# Carregar modelo pra realizar a predição
modelo_pontuacao = joblib.load('./modelo_regressao.pkl')

@app.post('/predict')
def predict(data: request_body):
    # preparar os dados para predição
    input_feature = [[data.horas_estudo]]

    # Realizar a predição
    y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)

    return {'pontuacao_teste': y_pred.tolist()}