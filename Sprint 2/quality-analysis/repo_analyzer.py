import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token token_token_toke"
}
PARAMS = {
    "q": "language:java",
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}

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

# Execução
top_repos = get_top_java_repositories()

# Mostra os 10 primeiros pra conferir
print(f"Total de repositórios obtidos: {len(top_repos)}")
print("Exemplo de repositórios:")
for repo in top_repos[:10]:
    print(repo)
