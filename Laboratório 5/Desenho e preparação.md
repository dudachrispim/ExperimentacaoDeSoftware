# GraphQL vs REST - Um experimento controlado

**LABORATÓRIO 05 - Desenho e Preparação do Experimento**

## 1. Desenho do Experimento

### A. Hipóteses

- **H₀ (Hipótese Nula):** Não há diferença significativa entre as APIs REST e GraphQL em tempo de resposta e tamanho da resposta.
- **H₁ (Hipótese Alternativa):** A API GraphQL possui menor tempo de resposta e tamanho de resposta comparado à API REST.

---

### B. Variáveis

- **Variáveis Dependentes:**
  - Tempo de resposta (ms)
  - Tamanho da resposta (bytes)

- **Variável Independente:**
  - Tipo de API (REST ou GraphQL)

---

### C. Tratamentos

- **Tratamento 1:** Requisições feitas à API REST.
- **Tratamento 2:** Requisições feitas à API GraphQL.

---

### D. Objetos Experimentais

- Uma aplicação com uma base de dados de livros.
- Ambas as APIs (REST e GraphQL) oferecem acesso aos mesmos dados.

---

### E. Tipo de Projeto Experimental

- Estudo controlado e comparativo com duas versões da API.

---

### F. Quantidade de Medições

- Serão realizadas 30 medições para cada tipo de API, totalizando 60 medições.

---

### G. Ameaças à Validade

- **Internas:** Variações na conexão ou desempenho local.
- **Externas:** Resultados podem não refletir cenários de produção.
- **Construção:** APIs podem ter diferenças de implementação que afetam o resultado.
- **Conclusão Estatística:** Número de amostras pode ser limitado para inferências fortes.

---

## 2. Preparação do Experimento

### a) Ambiente

- APIs implementadas localmente para minimizar ruídos externos.
- Frameworks utilizados:
  - Node.js com Express e Apollo Server (ou Python com Flask + Graphene)
- Banco de dados local ou simulado com dados estáticos.

---

### b) Ferramentas

- **Linguagem:** Python
- **Bibliotecas:** `requests`, `time`, `pandas`

---

### c) Script de Medição

Um script foi desenvolvido para realizar chamadas REST e GraphQL, medir o tempo de resposta e o tamanho da resposta.

#### Exemplo de chamada GraphQL usada:

```graphql
{
  book(id: 1) {
    title
    author {
      name
    }
    rating
  }
}
```
Exemplo de trecho do código:

```start = time.time()
response = requests.post(GRAPHQL_URL, json=GRAPHQL_QUERY)
end = time.time()
tempo_resposta = (end - start) * 1000
```

O script completo está disponível no arquivo experimento_tempo_resposta.py.

### d) Resultado Esperado
Uma tabela em .csv contendo os tempos de resposta e tamanhos para REST e GraphQL.

Esses dados serão usados para análise estatística na próxima sprint.

