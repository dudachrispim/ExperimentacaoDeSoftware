import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Estilo rosa 💗
rosa = "#e75480"
sns.set(style="whitegrid")

# Cria pasta se não existir
os.makedirs("graficos", exist_ok=True)

# Carrega o CSV final
df = pd.read_csv("repositorios_java_com_metricas_ck.csv")

# Remove valores ausentes
df = df.dropna(subset=["CBO médio", "DIT médio", "LCOM médio", "LOC médio"])

# Converte datas para calcular idade
df["Criado em"] = pd.to_datetime(df["Criado em"], errors="coerce")
df["Idade (anos)"] = (pd.Timestamp.today() - df["Criado em"]).dt.days / 365.25

# Gráficos principais
metricas_ck = ["CBO médio", "DIT médio", "LCOM médio", "LOC médio"]
metricas_proc = ["Estrelas", "Idade (anos)", "Tamanho (KB)"]

# Gráficos de dispersão 💗
for proc in metricas_proc:
    for qual in metricas_ck:
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=df, x=proc, y=qual, color=rosa, marker='X', s=40)
        plt.title(f"{proc} x {qual}")
        plt.tight_layout()
        plt.savefig(f"graficos/{proc}_x_{qual}.png")
        plt.close()

# Heatmap Pearson
plt.figure(figsize=(8, 6))
pearson_corr = df[metricas_proc + metricas_ck].corr(method='pearson')
sns.heatmap(pearson_corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlação (Pearson)")
plt.tight_layout()
plt.savefig("graficos/correlacao_pearson.png")
plt.close()

# Heatmap Spearman
plt.figure(figsize=(8, 6))
spearman_corr = df[metricas_proc + metricas_ck].corr(method='spearman')
sns.heatmap(spearman_corr, annot=True, cmap="viridis", fmt=".2f")
plt.title("Matriz de Correlação (Spearman)")
plt.tight_layout()
plt.savefig("graficos/correlacao_spearman.png")
plt.close()

print("✅ Gráficos gerados na pasta 'graficos'")
