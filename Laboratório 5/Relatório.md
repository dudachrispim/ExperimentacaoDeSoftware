# GraphQL vs REST - Um experimento controlado

**LABORATÓRIO 05 - Desenho e Preparação do Experimento**

## Introdução

Este relatório apresenta os resultados de um experimento controlado com o objetivo de comparar APIs REST e GraphQL. A proposta é avaliar se existem diferenças significativas entre elas no que se refere ao **tempo de resposta** e ao **tamanho da resposta** para consultas equivalentes.

As perguntas que guiam este estudo são:

- **RQ1:** As respostas às consultas GraphQL são mais rápidas que as de REST?
- **RQ2:** As respostas às consultas GraphQL têm tamanho menor que as de REST?

O experimento foi conduzido utilizando um sistema simulado de **livros e autores**, onde os dados foram expostos tanto por uma API REST quanto por uma API GraphQL.

---

## Metodologia

### Hipóteses

- **H0 (Nula):** Não há diferença significativa no tempo de resposta e no tamanho da resposta entre REST e GraphQL.
- **H1 (Alternativa):** GraphQL apresenta menor tempo de resposta e/ou menor tamanho de resposta que REST.

### Variáveis

- **Variáveis Independentes:**  
  Tipo de API utilizada (REST ou GraphQL).

- **Variáveis Dependentes:**  
  - Tempo de resposta (em milissegundos).  
  - Tamanho da resposta (em bytes).

### Tratamentos

- **Tratamento 1:** Consultas feitas à API REST (`GET /books/1`).
- **Tratamento 2:** Consultas feitas à API GraphQL (query para o livro de ID 1, solicitando `title`, `author.name` e `rating`).

### Objetos Experimentais

- Um serviço simulado de gestão de livros, contendo informações sobre livros, autores e avaliações (ratings).

### Tipo de Projeto Experimental

- **Experimento controlado** com medidas repetidas (30 execuções para cada API).

### Quantidade de Medições

- 30 requisições REST.  
- 30 requisições GraphQL.

### Ameaças à Validade

- **Validade interna:** Variações de carga no ambiente local (uso da máquina, rede).
- **Validade externa:** Resultados podem não se aplicar a outros domínios, modelos de dados maiores ou ambientes de produção.
- **Validade de construção:** As consultas em REST e GraphQL foram desenhadas para serem equivalentes, mas pequenas diferenças na estrutura de resposta podem ocorrer.

---

## Execução do Experimento

O experimento foi executado utilizando um script Python, desenvolvido para realizar 30 requisições para a API REST e 30 requisições para a API GraphQL, medindo o tempo de resposta (em milissegundos) e o tamanho da resposta (em bytes).

O arquivo de resultados gerado foi `resultados_experimento.csv`, contendo 60 linhas (30 REST e 30 GraphQL).

---

## Análise dos Resultados

### Revisão dos Dados

Os dados foram revisados para identificar outliers ou medições incorretas. Nenhuma anomalia relevante foi identificada.

---

### Resultados

| API      | Tempo Médio (ms) | Tamanho Médio (bytes) |
|-----------|-------------------|------------------------|
| REST      | 4,03              | 89                    |
| GraphQL   | 4,83              | 132                   |


- **Tempo de Resposta (RQ1):**  
 O REST apresentou um tempo médio ligeiramente menor que o GraphQL, indicando que, neste cenário simples, REST teve melhor desempenho em tempo de resposta.

![Tempo de resposta](https://github.com/user-attachments/assets/dad88f09-0f5f-4e4c-8623-0c2ecd8092d3)

- **Tamanho da Resposta (RQ2):**  
 As respostas do REST foram menores, pois retornam diretamente os dados do recurso `/books/1` de forma simples, sem a sobrecarga estrutural que o GraphQL possui (como os blocos `data`, `book` e outros metadados na resposta).

![Tamanho da resposta](https://github.com/user-attachments/assets/fe0fe6aa-2eef-4db0-a5b5-5a4557ae3b41)

Os resultados, de certa forma, contrariam a expectativa comum de que o GraphQL sempre terá respostas menores, evidenciando que em cenários muito simples e com dados pouco aninhados, o REST pode ser mais eficiente tanto em tempo quanto em tamanho de resposta.

No entanto, vale reforçar que, em sistemas maiores, com consultas mais complexas e dados muito aninhados, o benefício do GraphQL se torna mais evidente, já que ele permite ao cliente definir exatamente os campos que deseja, evitando overfetching (dados a mais) e underfetching (dados de menos).

---

## Conclusão

Com base nos dados analisados:
- O **REST apresentou, neste experimento, tempo de resposta menor e tamanho de resposta menor em relação ao GraphQL.**
- Portanto, **aceitamos a hipótese alternativa (H1) para o tempo de resposta e o tamanho, mas em favor do REST, e não do GraphQL.**

Isso demonstra que a escolha entre REST e GraphQL deve considerar o contexto, a complexidade das consultas e o tipo de aplicação desenvolvida.

---

## Arquivos Gerados

- `resultados_experimento.csv` — Resultados das medições (tempo e tamanho das respostas).
- `script_teste.py` — Script Python utilizado para executar o experimento.

