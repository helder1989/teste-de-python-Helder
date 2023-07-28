### Desenvolvimento de um aplicativo Web utilizando Python e Streamlit


O objetivo deste programa é criar um aplicativo da Web usando Python e a biblioteca Streamlit para implementar um modelo de aprendizado de máquina que faz previsões sobre a propensão de uma pessoa ao diabetes.

O aplicativo permite que o usuário insira informações relevantes (como níveis de glicose, pressão arterial, índice de massa corporal etc.) sobre a probabilidade de uma pessoa ter diabetes ou não.

O programa executa as seguintes etapas:

**1)** Carrega o conjunto de dados "diabetes.csv" do Kaggle, que contém informações sobre os pacientes e se eles têm ou não diabetes.

**2)** Exibe um campo de entrada para o usuário inserir seu nome.

**3)** Usa um modelo de aprendizado de máquina (Random Forest Classifier) ​​para treinar o modelo usando os dados disponíveis no conjunto de treinamento.

**4)** O modelo treinado é então usado para fazer previsões com base nos dados inseridos pelo usuário.

**5)** A precisão do modelo é calculada comparando as previsões feitas pelo modelo com os rótulos verdadeiros (diabetes ou não) dos dados do teste.

**6)** A precisão do modelo é exibida na tela, indicando a precisão das previsões.

Portanto, o programa permite que o usuário verifique interativamente se está propenso a ter diabetes com base nas informações inseridas.

É importante ressaltar que o aplicativo é uma demonstração simples, e muitos outros fatores podem influenciar no diagnóstico real do diabetes. Na prática, um modelo de aprendizado de máquina para diagnóstico médico requer uma avaliação mais abrangente, incluindo validação em conjuntos de dados independentes e consulta a profissionais de saúde qualificados.


