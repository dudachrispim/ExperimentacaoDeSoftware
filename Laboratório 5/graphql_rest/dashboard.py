import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('resultados_experimento.csv')

sns.set(style="whitegrid")

# Tempo de Resposta
plt.figure(figsize=(8, 6))
sns.boxplot(x="API", y="Tempo (ms)", data=df, palette="Set2")
plt.title("Tempo de Resposta: REST vs GraphQL")
plt.ylabel("Tempo (ms)")
plt.xlabel("API")
plt.savefig("tempo_resposta.png")
plt.show()

# Tamanho das Respostas
plt.figure(figsize=(8, 6))
sns.barplot(x="API", y="Tamanho (bytes)", data=df, palette="Set2", estimator="mean")
plt.title("Tamanho Médio das Respostas: REST vs GraphQL")
plt.ylabel("Tamanho (bytes)")
plt.xlabel("API")
plt.savefig("tamanho_resposta.png")
plt.show()

# Tabela
tabela = df.groupby("API").agg({
    "Tempo (ms)": ["mean", "min", "max", "std"],
    "Tamanho (bytes)": ["mean"]
}).round(2)

print("\nEstatísticas Descritivas:\n")
print(tabela)
