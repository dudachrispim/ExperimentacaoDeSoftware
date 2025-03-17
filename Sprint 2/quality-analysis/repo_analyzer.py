import requests
import subprocess
import os


GITHUB_API_URL = "https://api.github.com/search/repositories"
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token token_token_token"
}
PARAMS = {
    "q": "language:java",
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}
CLONE_DIR = "repositories"
CK_JAR_PATH = "ck.jar"


# Obter repositórios
def get_top_java_repositories():
    repositories = []
    for page in range(1, 11):  # 10 páginas para 1000 repositórios (100 por página)
        PARAMS["page"] = page
        response = requests.get(GITHUB_API_URL, headers=HEADERS, params=PARAMS)
        if response.status_code == 200:
            data = response.json()["items"]
            for repo in data:
                repositories.append(repo["clone_url"])
        else:
            print(f"Erro ao buscar repositórios: {response.status_code}")
            break
    return repositories


# Clonar repositórios
def clone_repositories(repositories):
    if not os.path.exists(CLONE_DIR):
        os.makedirs(CLONE_DIR)


    for repo_url in repositories[:5]:  # Clonando apenas 5 para teste
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = os.path.join(CLONE_DIR, repo_name)


        if not os.path.exists(repo_path):
            print(f"Clonando {repo_name}...")
            subprocess.run(["git", "clone", repo_url, repo_path])


# Rodar CK
def run_ck_analysis():
    for repo_name in os.listdir(CLONE_DIR):
        repo_path = os.path.join(CLONE_DIR, repo_name)
        print(f"Analisando {repo_name}...")
        subprocess.run(["java", "-jar", CK_JAR_PATH, repo_path, "true", "0", "false"])


# Execução
top_repos = get_top_java_repositories()
clone_repositories(top_repos)
run_ck_analysis()
