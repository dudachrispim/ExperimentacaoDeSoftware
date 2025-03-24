# Laboratório 2

### Um estudo das caracteristicas de qualidade de sistemas java


Estudo que visa de analisar repositórios relevantes, escritos na linguagem estudada, coletaremos os top-1.000 repositórios Java mais populares do GitHub, calculando cada uma das métricas propstas.


## Métricas 

Para cada questão de pesquisa, será realizada a comparação entre as características do processo de desenvolvimento dos repositórios e os valores obtidos para as métricas definidas nesta seção. 

Para as métricas de processo, tem-se:
• Popularidade: número de estrelas
• Tamanho: linhas de código (LOC) e linhas de comentários
• Atividade: número de releases
• Maturidade: idade (em anos) de cada repositório coletado

Por métricas de qualidade, tem-se:
• CBO: Coupling between objects
• DIT: Depth Inheritance Tree
• LCOM: Lack of Cohesion of Methods

## Questões de Pesquisa  

Desta forma, este laboratório tem o objetivo de responder às seguintes questões de pesquisa:

**RQ 01.** Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?
**RQ 02.** Qual a relação entre a maturidade do repositórios e as suas características de qualidade ?
**RQ 03.** Qual a relação entre a atividade dos repositórios e as suas características de qualidade?
**RQ 04.** Qual a relação entre o tamanho dos repositórios e as suas características de qualidade? 

---

## Dependências  

Para que o projeto funcione corretamente, é necessário realizar as seguintes importações:  

```
import requests
import csv
import os
import subprocess
```
---

## Configuração do ambiente  

Para rodar o projeto, crie um ambiente virtual seguindo os passos abaixo:  

### **1. Criar ambiente virtual**  
Abra o terminal e execute o comando:

```bash
python -m venv .venv
```
### **2. Ativar o ambiente virtual**

### No macOS e Linux:

```bash
source .venv/bin/activate
```

### No Windows:
```powershell
.venv\Scripts\Activate
```
### **3. Instalar as Dependências**  
Após ativar o ambiente virtual, instale as bibliotecas necessárias executando o comando abaixo:

```bash
pip install requests
```


### **4. Executar o Script**  
Após configurar o ambiente, instalar as dependências e configurar o token, execute o script principal do projeto com o seguinte comando:

```bash
python repo_analyzer.py
```
