# Relatório Final


## 1. Introdução

Este relatório apresenta a análise dos dados coletados de 1.000 repositórios Java do GitHub, com base em diversas métricas extraídas via API. As medições incluem informações sobre estrelas, forks, tamanho do repositório, entre outras. O objetivo é identificar padrões, correlações e levantar hipóteses sobre os dados.

## 2. Coleta de Dados

A coleta foi realizada utilizando a API do GitHub, buscando os repositórios mais populares em Java, ordenados pelo número de estrelas. Os seguintes atributos foram extraídos:

- Nome do repositório

- URL

- Estrelas

- Data de criação

- Última atualização

- Tamanho do repositório (KB)

- Forks

- Issues abertas

- Watchers

Além disso, um repositório de teste foi clonado para execução do CK, ferramenta que extrai métricas de qualidade de software.

## 3. Hipóteses

- **H1:** Com base nos dados coletados, foram formuladas as seguintes hipóteses:

- **H2:** Repositórios mais populares (com mais estrelas) tendem a ser maiores em tamanho.

- **H3:** Repositórios mais antigos possuem mais forks e watchers devido ao acúmulo de contribuições ao longo do tempo.

- **H4:** Repositórios com mais estrelas tendem a ter menos issues abertas, pois são mais bem mantidos.

- **H5:** Existe uma correlação entre o número de watchers e forks, indicando o interesse da comunidade.

- **H6:** Repositórios com maior atividade recente tendem a crescer em popularidade mais rapidamente.
