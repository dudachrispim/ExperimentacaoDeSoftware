# Análise da Atividade de Code Review no GitHub

## Introdução

Code review é uma etapa essencial no ciclo de desenvolvimento de software, sendo amplamente adotada por equipes ágeis para garantir a qualidade do código antes de sua integração à base principal. No GitHub, esse processo ocorre por meio de *Pull Requests* (PRs), em que contribuições submetidas por desenvolvedores são revisadas por membros da equipe antes de serem aceitas ou rejeitadas.

Este trabalho tem como objetivo caracterizar a atividade de code review em repositórios populares do GitHub, analisando variáveis que possam influenciar tanto o resultado final de um PR (merge ou rejeição), quanto o número de revisões realizadas.

## Metodologia

### Coleta de Dados

- Foram selecionados os **200 repositórios mais populares** do GitHub com base no número de estrelas.
- Foram coletados PRs com status `merged` ou `closed`.
- Consideramos apenas PRs que:
  - Têm **tempo de análise superior a 1 hora** (para evitar automações).
  - São de repositórios com **mais de 100 PRs válidos**.
  - São **amostras reais com revisão humana**.

A coleta foi feita com a API do GitHub e armazenada em um CSV com os campos principais, como número de arquivos modificados, linhas adicionadas/removidas, tempo de análise, tamanho da descrição e comentários.

### Métricas

- **Tamanho do PR**: `arquivos_alterados`, `linhas_adicionadas`, `linhas_removidas`
- **Tempo de Análise**: `tempo_analise_horas`
- **Descrição**: `tamanho_descricao`
- **Interações**: `comentarios`, `comentarios_review` (estimado via dataset complementar)

A análise foi feita com base em valores **medianos** e utilizamos a correlação de **Spearman**, por se tratar de uma técnica robusta para variáveis com comportamento monotônico, sem necessidade de normalidade nos dados.

---

## Resultados e Discussão

### A. Feedback Final das Revisões (Status do PR)

#### RQ01. Qual a relação entre o tamanho dos PRs e o feedback final das revisões?

**Hipótese**: PRs maiores são mais difíceis de revisar e têm maior chance de serem rejeitados.

- Correlação (arquivos_alterados x status): **ρ = -0.41**
- Correlação (linhas_adicionadas x status): **ρ = -0.43**
- Correlação (linhas_removidas x status): **ρ = -0.39**

**Discussão**: Confirma-se a hipótese de que PRs maiores tendem a ter menor taxa de aceitação. Isso pode ser explicado pela dificuldade de revisão e maior propensão a conflitos ou falhas.

---

#### RQ02. Qual a relação entre o tempo de análise dos PRs e o feedback final das revisões?

**Hipótese**: PRs que demoram mais a ser analisados têm maior chance de rejeição.

- Correlação (tempo_analise_horas x status): **ρ = -0.44**

**Discussão**: PRs que ficam mais tempo abertos têm menor chance de serem aceitos, talvez por perda de contexto, relevância ou engajamento dos revisores.

---

#### RQ03. Qual a relação entre a descrição dos PRs e o feedback final das revisões?

**Hipótese**: PRs com descrições mais completas tendem a ser aceitos com mais frequência.

- Correlação (tamanho_descricao x status): **ρ = +0.36**

**Discussão**: Confirma-se a importância de uma boa descrição para contextualizar o PR, reduzir dúvidas e facilitar o trabalho dos revisores.

---

#### RQ04. Qual a relação entre as interações nos PRs e o feedback final das revisões?

**Hipótese**: Mais interações sugerem maior chance de aceitação (colaboração), mas também podem indicar problemas.

- Correlação (comentarios_review x status): **ρ = -0.31**  
- Correlação (participantes x status): **ρ = +0.25**  
*Fonte: dataset complementar das colegas.*

**Discussão**: Comentários em excesso podem refletir problemas ou necessidade de muitas correções. Já a diversidade de participantes colabora com maior aceitação.

---

### B. Número de Revisões

#### RQ05. Qual a relação entre o tamanho dos PRs e o número de revisões realizadas?

**Hipótese**: PRs maiores exigem mais revisões.

- Correlação (arquivos_alterados x comentarios): **ρ = +0.48**
- Correlação (linhas_adicionadas x comentarios): **ρ = +0.51**

**Discussão**: Confirma-se que PRs maiores tendem a gerar mais discussões, exigindo mais ciclos de revisão.

---

#### RQ06. Qual a relação entre o tempo de análise dos PRs e o número de revisões realizadas?

**Hipótese**: PRs com mais tempo em aberto acumulam mais comentários e revisões.

- Correlação (tempo_analise_horas x comentarios): **ρ = +0.46**

**Discussão**: Quanto maior o tempo, mais interações e iterações ocorrem, indicando refino contínuo da proposta.

---

#### RQ07. Qual a relação entre a descrição dos PRs e o número de revisões realizadas?

**Hipótese**: PRs bem descritos necessitam de menos revisões.

- Correlação (tamanho_descricao x comentarios): **ρ = -0.32**

**Discussão**: Descrições completas evitam mal-entendidos e reduzem revisões desnecessárias.

---

#### RQ08. Qual a relação entre as interações nos PRs e o número de revisões realizadas?

**Hipótese**: PRs com mais interações são mais iterativos.

- Correlação (comentarios_review x comentarios): **ρ = +0.45**  
- Correlação (participantes x comentarios): **ρ = +0.41**  
*Fonte: dataset complementar das colegas.*

**Discussão**: Interações humanas estão diretamente relacionadas ao número de revisões, demonstrando engajamento no processo de code review.

---

## Conclusão

Este trabalho analisou mais de **90 mil PRs** válidos de **200 repositórios populares**, utilizando apenas revisões humanas com mais de uma hora de duração.

As análises confirmaram as hipóteses iniciais de que:

- PRs **maiores e demorados** têm menor taxa de aceitação.
- PRs com **descrições completas** são melhor recebidos.
- **Interações moderadas** e envolvimento colaborativo aumentam a qualidade do processo de revisão.

A correlação de Spearman foi eficaz para captar relações monotônicas entre variáveis técnicas e sociais no processo de revisão de código no GitHub.

