# TP1 – Floating Point Associativity Test

## Objectif
Ce projet teste deux problèmes : 
si l’addition en virgule flottante est **associative** :  
> Est-ce que `(x + y) + z == x + (y + z)` est toujours vrai ?

Et le problème bancaire : 
“My banker proposed this investment to me:
You give me e ≈ 2.71828...
The following year, I take 1 euro as a fee and multiply by 1.
The next year, I take 1 euro as a fee and multiply by 2.
The next year, I take 1 euro as a fee and multiply by 3.
...
After n years, I take 1 euro as a fee and multiply by n.
To retrieve my money, there is a 1 euro fee.
In 50 years, for my retirement, how much money will I have?”


---

## Project structure
```bash

.github/workflows/         # Contient les workflows GitHub Actions
  └─ run_tp1.yml           # Workflow pour exécuter les tests et générer les résultats

.ipynb_checkpoints/        # Dossier automatique Jupyter pour sauvegardes intermédiaires

banking_experiment/        # Expérience banking
  ├─ analyze_variability.ipynb       # Notebook d'analyse de variabilité pour banking
  ├─ banking_property_template.py.jinja  # Template Jinja pour générer les simulations
  ├─ generate_and_run_all_banking.py     # Script d'orchestration pour toutes les combinaisons
  ├─ package-lock.json                 # Dépendances Node (si nécessaire pour certains outils)
  ├─ tp1_banker.py                     # Script Python simulant le problème bancaire
  └─ variability_results_banking.csv   # Résultats de la simulation banking

venv/                         # Environnement virtuel Python (local)

Autres fichiers principaux :
- analyze_variability.ipynb     # Notebook pour l'analyse globale
- answer_associativity.txt      # Réponses / notes associativité
- answer_associativity_llm.txt # Notes associativité avec LLM
- Dockerfile                    # Contient les instructions pour exécuter les deux expériences
- generate_and_run_all.py       # Orchestrateur pour le problème d'associativité
- LLM_associativity.md          # Notes sur l'analyse LLM associativité
- nixpkgs-pin.nix / nixpkgs-pin.nix.bak  # Configs pour Nix (reproductibilité environnement)
- property_template.py.jinja    # Template Jinja pour l'expérience associativité
- shell.nix                     # Script Nix pour l'environnement
- tp1_associativity.py          # Script Python associativité
- tp1_associativity_go.go       # Script Go associativité
- variability_results.csv       # Résultats associativité
```

---

## ⚙️ Exécution rapide

### 🐍 Python
```bash
python3 banking_experiment/generate_and_run_all_banking.py
python3 generate_and_run_all.py
```

# Go 
```bash
go run tp1_associativity_go.go
```

# Docker
```bash
docker build -t reproducibility_lab .
docker run --rm -v $(pwd):/usr/src/app/out reproducibility_lab
```


## Les résultats sont enregistrés dans :
- answer_associativity.txt
- answer_associativity_llm.txt