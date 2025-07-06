# Aplicativo de Classificação de Sentimentos 💬🔍

Esta é uma aplicação full stack que utiliza um modelo de machine learning treinado para classificar o sentimento (positivo ou negativo) de um texto inserido pelo usuário.

## Visão Geral

O projeto consiste na construção de um modelo de machine learning utilizando algoritmos clássicos (Naive Bayes, LinearSVC, KNN, Árvore de Decisão) para realizar a classificação de sentimentos. O modelo é treinado com vetorização TF-IDF e otimizado usando GridSearchCV com validação cruzada. O pipeline com melhor desempenho (vetorizador + modelo) é exportado utilizando `joblib`.

O back-end em Flask disponibiliza o modelo e expõe o endpoint `/predict`. Um front-end simples em HTML + JavaScript permite que os usuários insiram textos e visualizem a predição do sentimento.

## Estrutura do Projeto

```
sentiment_app/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── model/
│       └── sentiment_model.pkl
├── frontend/
│   └── index.html
├── tests/
│   └── test_model.py
```

## Como Executar

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd ../frontend
open index.html  # Ou clique duas vezes no arquivo
```

### Teste Automatizado

```bash
cd ../tests
pytest test_model.py
```

## Resultados de Linha de Base (Exemplo)

| Modelo             | Acurácia | F1-score |
|--------------------|----------|----------|
| Naive Bayes        | 0.85     | 0.86     |
| SVM                | 0.84     | 0.85     |
| KNN                | 0.58     | 0.70     |
| Árvore de Decisão  | 0.76     | 0.78     |
--------------------------------------------

## Reflexão: Boas Práticas de Desenvolvimento Seguro no Projeto de Classificação de Sentimentos
No contexto do projeto de classificação de sentimentos, aplicar boas práticas de segurança é essencial, mesmo em ambientes de demonstração. Caso fossem utilizados dados reais de usuários, técnicas de anonimização (como remoção de nomes ou e-mails com NLP) evitariam vazamentos de informações pessoais.

Além disso, a validação e sanitização das entradas no front-end e no back-end previnem ataques como XSS ou falhas por dados malformados. A minimização de dados, armazenando apenas o necessário para a predição, reduz riscos em caso de vazamento.

A aplicação também deve usar CORS bem configurado e manter o modelo (.pkl) em locais protegidos no servidor. Por fim, boas práticas como monitoramento de uso da API e log seguro das predições ajudam a manter o controle e a integridade do sistema em ambientes reais.


## 👤 Autor

Juliaana M. Pereira
