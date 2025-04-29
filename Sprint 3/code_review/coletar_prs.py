import requests
import time
import pandas as pd
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

TOKEN = "" 
HEADERS = {"Authorization": f"token {TOKEN}"}

def create_session():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1,
                    status_forcelist=[429, 500, 502, 503, 504],
                    allowed_methods=["GET"])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    return session

session = create_session()

def get_repos_in_batches(total_repos=200, per_page=50):
    """
    Coleta repositórios em batches usando a query 'stars:>500' para obter um número maior de repositórios.
    Cada batch é salvo em um arquivo separado e todos são combinados no arquivo 'repositorios.txt'.
    """
    repos = []
    num_batches = (total_repos // per_page) + (1 if total_repos % per_page != 0 else 0)
    for batch in range(1, num_batches + 1):
        url = (f"https://api.github.com/search/repositories?q=stars:>500&sort=stars"
               f"&order=desc&per_page={per_page}&page={batch}")
        try:
            r = session.get(url, headers=HEADERS, timeout=10)
            r.raise_for_status()
            data = r.json()
            batch_repos = [item["full_name"] for item in data.get("items", [])]
            repos.extend(batch_repos)
            with open(f"repositorios_batch_{batch}.txt", "w", encoding="utf-8") as f:
                for repo in batch_repos:
                    f.write(repo + "\n")
            print(f"Batch {batch}/{num_batches} coletado: {len(batch_repos)} repositórios.")
            time.sleep(2)
        except Exception as e:
            print(f"Erro no batch {batch}: {e}")
            break
    repos = repos[:total_repos]
    with open("repositorios.txt", "w", encoding="utf-8") as f:
        for repo in repos:
            f.write(repo + "\n")
    print("Todos os repositórios coletados e salvos em repositorios.txt.")
    return repos

def get_pr_details(repo, pr_number):
    """
    Faz uma chamada para obter os detalhes do PR, incluindo changed_files, additions e deletions.
    """
    detail_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    try:
        r = session.get(detail_url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Erro ao obter detalhes do PR #{pr_number} em {repo}: {e}")
        return None

def get_pull_requests(repo, max_pages=5):
    """
    Coleta os pull requests de um repositório, iterando por até max_pages.
    Isso serve como uma amostra representativa para a análise.
    Os dados são acumulados e, ao final, retornados.
    """
    print(f"\n--- Iniciando coleta de PRs para o repositório: {repo} ---")
    pulls = []
    page = 1
    while page <= max_pages:
        url = f"https://api.github.com/repos/{repo}/pulls?state=all&per_page=100&page={page}"
        try:
            r = session.get(url, headers=HEADERS, timeout=10)
            r.raise_for_status()
            pr_list = r.json()
        except Exception as e:
            print(f"Erro ao acessar PRs de {repo} na página {page}: {e}")
            break

        if not isinstance(pr_list, list) or len(pr_list) == 0:
            print(f"Nenhum PR retornado na página {page} de {repo}.")
            break

        print(f"Processando página {page} para {repo} com {len(pr_list)} PRs.")
        for pr in pr_list:
            try:
                pr_number = pr.get("number")
                created_at = pr.get("created_at")
                closed_at = pr.get("closed_at") or pr.get("merged_at")
                if created_at and closed_at:
                    created = datetime.fromisoformat(created_at.replace("Z","+00:00"))
                    closed = datetime.fromisoformat(closed_at.replace("Z","+00:00"))
                    tempo_analise = (closed - created).total_seconds() / 3600
                else:
                    tempo_analise = 0

                print(f"Repo: {repo} PR #{pr_number}: tempo {tempo_analise:.2f}h, review_comments: {pr.get('review_comments', 0)}")

                pr_detail = get_pr_details(repo, pr_number)
                if pr_detail is None or "changed_files" not in pr_detail:
                    print(f"Detalhes ausentes para PR #{pr_number} em {repo}, pulando...")
                    continue

                pulls.append({
                    "repo": repo,
                    "pr_number": pr_number,
                    "url": pr.get("html_url"),
                    "state": pr.get("state"),
                    "merged": pr.get("merged_at") is not None,
                    "created_at": created_at,
                    "closed_at": pr.get("closed_at"),
                    "merged_at": pr.get("merged_at"),
                    "tempo_analise_horas": round(tempo_analise, 2),
                    "arquivos_alterados": pr_detail.get("changed_files", 0),
                    "linhas_adicionadas": pr_detail.get("additions", 0),
                    "linhas_removidas": pr_detail.get("deletions", 0),
                    "tamanho_descricao": len(pr.get("body") or ""),
                    "comentarios": pr.get("comments", 0),
                    "comentarios_review": pr.get("review_comments", 0),
                    "autor": pr.get("user", {}).get("login", "")
                })
                time.sleep(0.5)
            except Exception as e:
                print(f"Erro ao processar PR {pr.get('number')} do repositório {repo}: {e}")
        print(f"Fim da página {page} para o repositório {repo}.")
        page += 1
        time.sleep(1)
    print(f"--- Fim da coleta de PRs para o repositório: {repo} ---\n")
    return pulls

def main():
    repos = get_repos_in_batches(total_repos=200, per_page=50)

    all_prs = []
    for repo in repos:
        pr_data = get_pull_requests(repo, max_pages=5)
        print(f"Coletados {len(pr_data)} PRs de {repo}.")
        all_prs.extend(pr_data)

    if all_prs:
        df = pd.DataFrame(all_prs)
        df.to_csv("dataset_prs.csv", index=False, encoding="utf-8")
        print("Dataset salvo como dataset_prs.csv.")
    else:
        print("Nenhum PR coletado.")

    print("=== Fim da coleta de todos os PRs ===")

if __name__ == "__main__":
    main()
