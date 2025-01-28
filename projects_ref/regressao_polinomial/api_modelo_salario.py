# Construindo a API
#Vamos aprender como entregar um modelo de machine learning através de uma aplicação usando o Streamlit. 
# Vamos criar uma API usando o FastAPI para receber os dados de entrada, carregar o modelo treinado e fazer a predição. 
# Para isso, vamos importar as bibliotecas necessárias, criar uma instância do FastAPI, definir a classe para validação dos dados de entrada e criar a função de predição. 
# Por fim, vamos decorar a função com o decorador do FastAPI para expor a função como uma API REST.
from fastapi import FastAPI
import joblib
# Instância do FastAPI
app = FastAPI()

# Classe que terá od dados do request body para API
from pydantic import BaseModel
class request_body(BaseModel):
    tempo_na_empresa: int
    nivel_na_empresa: int

# Carregar modelo pra realizar a predição

modelo_reg_poly = joblib.load('./modelo_salario.pkl')

@app.post('/predict')
def predict(data: request_body):
    # preparar os dados para predição
    input_features = {
        'tempo_na_empresa': data.tempo_na_empresa,
        'nivel_na_empresa': data.nivel_na_empresa
    }

    pred_df = pd.DataFrame(input_features, index=[1])

    # Realizar a predição
    y_pred = modelo_reg_poly.predict(pred_df)[0].astype(float)

    return {'salario_em_reais': y_pred.tolist()}