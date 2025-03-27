# Relatório Final

## 1. Introdução

Este relatório apresenta a análise dos dados coletados de 1.000 repositórios Java do GitHub, com base em diversas métricas extraídas via API. As medições incluem informações sobre estrelas, forks, tamanho do repositório, entre outras. O objetivo é identificar padrões, correlações e levantar hipóteses sobre os dados.

Além disso, este estudo busca compreender como características como popularidade, idade, tamanho e atividade dos repositórios se relacionam com métricas de qualidade de código obtidas por análise estática com a ferramenta CK.

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
- Commits  
- Releases

Em seguida, os repositórios foram clonados e analisados por meio da ferramenta **CK (CKJM Extended)**, que extrai métricas de qualidade de software, como acoplamento, herança, coesão e linhas de código.

## 3. Hipóteses

Com base nos dados coletados, foram formuladas as seguintes hipóteses:

- **H1:** Repositórios populares devem ter melhor qualidade de código, pois recebem mais colaborações e revisões.
- **H2:** Repositórios mais populares (com mais estrelas) tendem a ser maiores em tamanho.
- **H3:** Repositórios mais antigos possuem mais forks e watchers devido ao acúmulo de contribuições ao longo do tempo.
- **H4:** Repositórios com mais estrelas tendem a ter menos issues abertas, pois são mais bem mantidos.
- **H5:** Existe uma correlação entre o número de watchers e forks, indicando o interesse da comunidade.
- **H6:** Repositórios com maior atividade recente tendem a crescer em popularidade mais rapidamente.

## 4. Análise dos Dados

### RQ01: Qual a relação entre a popularidade dos repositórios e suas características de qualidade?

**Popularidade (Estrelas)**  
- Média: 8.978  
- Mediana: 5.529  
- Desvio padrão: 10.745

**CBO médio**  
- Média: 5.25  
- Mediana: 5.21  
- Desvio padrão: 1.74

![RQ01](graficos/apresentacao_rq01_estrelas_x_cbo.png)

A correlação de Pearson foi **-0.10** e a de Spearman **0.01**, indicando que não há uma relação forte entre popularidade e qualidade do código. Ou seja, repositórios populares não necessariamente têm menor acoplamento.

---

### RQ02: Qual a relação entre a maturidade dos repositórios e suas características de qualidade?

**Idade (anos)**  
- Média: 9.23  
- Mediana: 9.27  
- Desvio padrão: 2.90

**DIT médio**  
- Média: 1.46  
- Mediana: 1.39  
- Desvio padrão: 0.36

![RQ02](graficos/apresentacao_rq02_idade_x_dit.png)

A comparação entre idade (anos) e DIT médio mostrou uma correlação de **0.18 (Pearson)** e **0.27 (Spearman)**. Isso sugere que repositórios mais antigos têm tendência leve a maior profundidade de herança, mas não é uma relação forte.

---

### RQ03: Qual a relação entre a atividade dos repositórios e suas características de qualidade?

**Commits**  
- Média: 4.961  
- Mediana: 659.0  
- Desvio padrão: 36.156

**LCOM médio**  
- Média: 118.72  
- Mediana: 22.96  
- Desvio padrão: 1858.63

![RQ03](graficos/apresentacao_rq03_commits_x_lcom.png)

A correlação entre commits e LCOM médio foi **0.01 (Pearson)** e **0.36 (Spearman)**. A correlação moderada com Spearman indica que repositórios mais ativos tendem a ser um pouco mais coesos, mas não é uma relação garantida.

---

### RQ04: Qual a relação entre o tamanho dos repositórios e suas características de qualidade?

**Tamanho (KB)**  
- Média: 132.920  
- Mediana: 17.001  
- Desvio padrão: 709.581

**LOC médio**  
- Média: 50.27  
- Mediana: 43.5  
- Desvio padrão: 30.71

![RQ04](graficos/apresentacao_rq04_tamanho_x_loc.png)

A relação entre tamanho (KB) e LOC médio teve correlação de **0.05 (Pearson)** e **0.32 (Spearman)**. Isso indica que repositórios maiores tendem a conter arquivos com mais linhas de código, mas o crescimento do tamanho não está fortemente ligado a mudanças nas outras métricas de qualidade.

---

### Matriz de Correlação

#### Pearson
![Correlação Pearson](graficos/correlacao_pearson.png)

#### Spearman
![Correlação Spearman](graficos/correlacao_spearman.png)

## 5. Conclusão

Este estudo permitiu compreender melhor o ecossistema de repositórios Java no GitHub. Os resultados mostraram que a popularidade de um repositório está ligada a outros atributos como tamanho e atividade, mas **não necessariamente à qualidade de código** medida por métricas estáticas.

As correlações encontradas foram em geral fracas ou moderadas. Métricas como **LCOM** e **CBO** variam muito entre projetos, e parecem depender mais da organização interna e práticas da equipe do que da popularidade do repositório.
