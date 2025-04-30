# Análise da Atividade de Code Review no GitHub

## Introdução

Code review é uma etapa essencial no ciclo de desenvolvimento de software, sendo amplamente adotada por equipes ágeis para garantir a qualidade do código antes de sua integração à base principal. No GitHub, esse processo ocorre por meio de *Pull Requests* (PRs), em que contribuições submetidas por desenvolvedores são revisadas por membros da equipe antes de serem aceitas ou rejeitadas.

Este trabalho tem como objetivo caracterizar a atividade de code review em repositórios populares do GitHub, analisando variáveis que possam influenciar tanto o resultado final de um PR (merge ou rejeição), quanto o número de revisões realizadas.

## Metodologia

### Coleta de Dados

- Foram selecionados os **200 repositórios mais populares** do GitHub com base no número de estrelas.
- Foram coletados PRs com status `merged` ou `closed`.
- Consideramos apenas repositórios com **mais de 100 PRs válidos**.

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
![output](https://github.com/user-attachments/assets/8789778c-97cf-49a0-8e69-9d98d2f3ca0b)

---

#### RQ02. Qual a relação entre o tempo de análise dos PRs e o feedback final das revisões?

**Hipótese**: PRs que demoram mais a ser analisados têm maior chance de rejeição.

- Correlação (tempo_analise_horas x status): **ρ = -0.44**

**Discussão**: PRs que ficam mais tempo abertos têm menor chance de serem aceitos, talvez por perda de contexto, relevância ou engajamento dos revisores.
![output (1)](https://github.com/user-attachments/assets/2d431af7-90fe-465e-990e-36700ab20bed)

---

#### RQ03. Qual a relação entre a descrição dos PRs e o feedback final das revisões?

**Hipótese**: PRs com descrições mais completas tendem a ser aceitos com mais frequência.

- Correlação (tamanho_descricao x status): **ρ = +0.36**

**Discussão**: Confirma-se a importância de uma boa descrição para contextualizar o PR, reduzir dúvidas e facilitar o trabalho dos revisores.
![output (2)](https://github.com/user-attachments/assets/390cd102-d8dd-4bb9-a494-9df8b32da19e)

---

#### RQ04. Qual a relação entre as interações nos PRs e o feedback final das revisões?

**Hipótese**: Mais interações sugerem maior chance de aceitação (colaboração), mas também podem indicar problemas.

- Correlação (comentarios_review x status): **ρ = -0.31**  
- Correlação (participantes x status): **ρ = +0.25**  
*Fonte: dataset complementar das colegas.*

**Discussão**: Comentários em excesso podem refletir problemas ou necessidade de muitas correções. Já a diversidade de participantes colabora com maior aceitação.
![output (3)](https://github.com/user-attachments/assets/28fc7102-0b11-4a48-9801-4249c9c1c2d0)

---

### B. Número de Revisões

#### RQ05. Qual a relação entre o tamanho dos PRs e o número de revisões realizadas?

**Hipótese**: PRs maiores exigem mais revisões.

- Correlação (arquivos_alterados x comentarios): **ρ = +0.48**
- Correlação (linhas_adicionadas x comentarios): **ρ = +0.51**

**Discussão**: Confirma-se que PRs maiores tendem a gerar mais discussões, exigindo mais ciclos de revisão.
![output (4)](https://github.com/user-attachments/assets/0665cf9a-f121-48fd-91ca-f830546db29e)

---

#### RQ06. Qual a relação entre o tempo de análise dos PRs e o número de revisões realizadas?

**Hipótese**: PRs com mais tempo em aberto acumulam mais comentários e revisões.

- Correlação (tempo_analise_horas x comentarios): **ρ = +0.46**

**Discussão**: Quanto maior o tempo, mais interações e iterações ocorrem, indicando refino contínuo da proposta.
![output (5)](https://github.com/user-attachments/assets/c6f6e9e6-aeea-47c7-9207-17b1f1c30a8d)

---

#### RQ07. Qual a relação entre a descrição dos PRs e o número de revisões realizadas?

**Hipótese**: PRs bem descritos necessitam de menos revisões.

- Correlação (tamanho_descricao x comentarios): **ρ = -0.32**

**Discussão**: Descrições completas evitam mal-entendidos e reduzem revisões desnecessárias.
![output (6)](https://github.com/user-attachments/assets/aa1945e0-5a6d-4548-b061-88f33351a2c8)

---

#### RQ08. Qual a relação entre as interações nos PRs e o número de revisões realizadas?

**Hipótese**: PRs com mais interações são mais iterativos.

- Correlação (comentarios_review x comentarios): **ρ = +0.45**  
- Correlação (participantes x comentarios): **ρ = +0.41**  
*Fonte: dataset complementar das colegas.*

**Discussão**: Interações humanas estão diretamente relacionadas ao número de revisões, demonstrando engajamento no processo de code review.
![output (7)](https://github.com/user-attachments/assets/b753944d-d00e-4709-a4f1-7e3847c29814)

---

## Conclusão

As análises confirmaram as hipóteses iniciais de que:

- PRs **maiores e demorados** têm menor taxa de aceitação.
- PRs com **descrições completas** são melhor recebidos.
- **Interações moderadas** e envolvimento colaborativo aumentam a qualidade do processo de revisão.

A correlação de Spearman foi eficaz para captar relações monotônicas entre variáveis técnicas e sociais no processo de revisão de código no GitHub.

