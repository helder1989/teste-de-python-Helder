
# Import bibliotecas

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Título do aplicativo
st.title("Prevendo Diabetes")

# leitura da base de dados
@st.cache
def carregar_dados():
    data = pd.read_csv("diabetes.csv")
    return data

dados = carregar_dados()

# interagindo com o usuário
nome_usuario = st.text_input("Digite o seu nome:")

# nome do usuário na tela
st.write(f"Olá, {nome_usuario}!")

# Separando os dados em features (X) e target (y)
X = dados.drop("Outcome", axis=1)
y = dados["Outcome"]

# Divisão dos dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo de aprendizado de máquina (Random Forest)

modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Realizando a previsão com os dados de teste
y_pred = modelo.predict(X_test)

# Calculando a acurácia do modelo
acuracia = accuracy_score(y_test, y_pred)

# Exibição a acurácia do modelo na tela
st.write(f"A acurácia do modelo é de: {acuracia:.2f}")

