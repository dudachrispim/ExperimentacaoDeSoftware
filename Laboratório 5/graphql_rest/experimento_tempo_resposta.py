import requests
import time
import pandas as pd

REST_URL = 'http://localhost:3000/books/1'
GRAPHQL_URL = 'http://localhost:3000/graphql'
GRAPHQL_QUERY = {
    "query": """
    {
      book(id: 1) {
        title
        author {
          name
        }
        rating
      }
    }
    """
}

# REST
def test_rest():
    durations = []
    sizes = []
    for _ in range(30):
        start = time.time()
        r = requests.get(REST_URL)
        end = time.time()
        durations.append((end - start) * 1000)
        sizes.append(len(r.content))
    return durations, sizes

# GraphQL
def test_graphql():
    durations = []
    sizes = []
    for _ in range(30):
        start = time.time()
        r = requests.post(GRAPHQL_URL, json=GRAPHQL_QUERY)
        end = time.time()
        durations.append((end - start) * 1000)
        sizes.append(len(r.content))
    return durations, sizes

rest_time, rest_size = test_rest()
graphql_time, graphql_size = test_graphql()

df = pd.DataFrame({
    "API": ["REST"] * 30 + ["GraphQL"] * 30,
    "Tempo (ms)": rest_time + graphql_time,
    "Tamanho (bytes)": rest_size + graphql_size
})
df.to_csv("resultados_experimento.csv", index=False)