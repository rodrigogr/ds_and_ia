import streamlit as st
import json
import requests

# 1. Contruindo o Frond-End
# 1.1 - Formulário de Entrada

# Título da aplicação
st.title("Modelo de Predição de Salário")

# Inputs do Usuário
st.write("Quantos meses o profissional está na empresa?")
tempo_na_empresa = st.slider("Meses", min_value=1, max_value=120, value=60, step=1)

st.write("Qual o nível do profissional na empresa")
nivel_na_empresa = st.slider("Nível", min_value=1, max_value=120, value=60, step=1)

# Preparar dados para API
input_features = {'tempo_ba_empresa': tempo_na_empresa,
                  'nivel_na_empresa': nivel_na_empresa}

# 1.2 - Botão
if st.button('Estimar Salário'):
    res = request.post(url="http://127.0.0.1:8000/predict", data=json.dumps(input_features))
    res_json = json.loads(res.text)
    salario_em_reais = round(res_json['salario_em_reais'], 2)
    st.subheader(f'O Salário estimado é de R$ {salario_em_reais}')