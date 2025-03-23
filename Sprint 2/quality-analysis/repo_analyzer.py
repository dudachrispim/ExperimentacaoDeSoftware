import requests
import csv
import os
import subprocess

GITHUB_API_URL = "https://api.github.com/search/repositories"
HEADERS = {"Accept": "application/vnd.github.v3+json"}
PARAMS = {
    "q": "language:java",
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}

CLONE_DIR = "repositories"
CK_JAR_PATH = "ck/ck.jar"
OUTPUT_DIR = "ck_results"

# Lista para armazenar os repositórios
repos = []

# Coleta os 1.000 repositórios (10 páginas)
for page in range(1, 11):
    PARAMS["page"] = page
    response = requests.get(GITHUB_API_URL, headers=HEADERS, params=PARAMS)

    if response.status_code == 200:
        data = response.json()
        for repo in data["items"]:
            repos.append([repo["full_name"], repo["clone_url"], repo["stargazers_count"],
                          repo["created_at"], repo["updated_at"], repo["size"],
                          repo["forks_count"], repo["open_issues_count"], repo["watchers_count"]])
    else:
        print(f"Erro ao buscar página {page}: {response.status_code}")
        break

repos_csv = "repositorios_java.csv"
with open(repos_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "URL", "Estrelas", "Criado em", "Última atualização", "Tamanho (KB)", "Forks", "Issues abertas", "Watchers"])
    writer.writerows(repos)

print(f"Arquivo '{repos_csv}' criado com sucesso!")

# Clona um repositório de teste
if not os.path.exists(CLONE_DIR):
    os.makedirs(CLONE_DIR)

repo_test = repos[0][1]
repo_name = repos[0][0].split('/')[-1]
repo_path = os.path.join(CLONE_DIR, repo_name)

if not os.path.exists(repo_path):
    print(f"Clonando {repo_test}...")
    subprocess.run(["git", "clone", repo_test, repo_path])

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print("Rodando CK...")
subprocess.run(["java", "-jar", CK_JAR_PATH, repo_path, "true", "0", "false", OUTPUT_DIR])

print("Análise concluída! Arquivos CSV gerados na pasta ck_results.")
