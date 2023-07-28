
import pandas as pd

# Carregando os dados
data = pd.read_csv("diabetes.csv")

# Explorando os dados

# Visualizando as primeiras linhas
print(data.head())

# observando o resumo estatístico
print(data.describe())

# Verificando as informações sobre o tipo de dados e a contagem de valores não nulos em cada coluna
print(data.info())

# Verificando a contagem de valores ausentes em cada coluna.
print(data.isnull().sum())

# analisando se há valores duplicados no conjunto de dados.
print(data.duplicated().sum())

# verificando a distribuição das classes da variável de destino.
# Para garantir que não haja desequilíbrio de classe.
print(data['Outcome'].value_counts())






