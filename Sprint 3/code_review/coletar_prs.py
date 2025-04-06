import requests
import time
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}"}

def get_popular_repos(top_n=50):
    repos = []
    for page in range(1, (top_n // 100) + 2):
        url = f"https://api.github.com/search/repositories?q=stars:>1000&sort=stars&order=desc&per_page=100&page={page}"
        resp = requests.get(url, headers=HEADERS).json()
        repos += [item["full_name"] for item in resp.get("items", [])]
        time.sleep(2)
    return repos[:top_n]

def save_repos_to_txt(repos):
    with open("repositorios.txt", "w") as file:
        for repo in repos:
            file.write(repo + "\n")

def get_pull_requests(repo):
    print(f"Coletando PRs de: {repo}")
    pulls = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{repo}/pulls?state=all&per_page=100&page={page}"
        resp = requests.get(url, headers=HEADERS).json()

        if not isinstance(resp, list):
            break  # erro, limite, ou final

        for pr in resp:
            created = datetime.fromisoformat(pr["created_at"].replace("Z", "+00:00"))
            closed_or_merged = pr.get("closed_at") or pr.get("merged_at")
            if closed_or_merged:
                closed = datetime.fromisoformat(closed_or_merged.replace("Z", "+00:00"))
                time_diff_hours = (closed - created).total_seconds() / 3600
                if pr.get("review_comments", 0) >= 1 and time_diff_hours >= 1:
                    pulls.append({
                        "repo": repo,
                        "url": pr["html_url"],
                        "state": pr["state"],
                        "merged": pr["merged_at"] is not None,
                        "created_at": pr["created_at"],
                        "closed_at": pr["closed_at"],
                        "merged_at": pr["merged_at"],
                        "tempo_analise_horas": round(time_diff_hours, 2),
                        "arquivos_alterados": pr["changed_files"],
                        "linhas_adicionadas": pr["additions"],
                        "linhas_removidas": pr["deletions"],
                        "tamanho_descricao": len(pr["body"] or ""),
                        "comentarios": pr["comments"],
                        "comentarios_review": pr["review_comments"],
                        "autor": pr["user"]["login"]
                    })
        if len(resp) < 100:
            break
        page += 1
        time.sleep(1)
    return pulls

def main():
    # Etapa 1: Buscar repositórios
    repos = get_popular_repos(10)  # pode aumentar depois
    save_repos_to_txt(repos)

    # Etapa 2: Coletar PRs e métricas
    all_prs = []
    for repo in repos:
        prs = get_pull_requests(repo)
        all_prs.extend(prs)
        print(f"{len(prs)} PRs coletados de {repo}")

    # Salvar em CSV
    df = pd.DataFrame(all_prs)
    df.to_csv("dataset_prs.csv", index=False)
    print("Dataset salvo como dataset_prs.csv")

if __name__ == "__main__":
    main()
