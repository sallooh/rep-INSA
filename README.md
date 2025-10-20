# TP1 – Floating Point Associativity Test

## Objectif
Ce projet teste si l’addition en virgule flottante est **associative** :  
> Est-ce que `(x + y) + z == x + (y + z)` est toujours vrai ?

En pratique, à cause des erreurs d’arrondi, la réponse est **non**.  
Le programme mesure la fréquence à laquelle cette égalité est respectée.

---

## Contenu
- `tp1_associativity.py` → version **Python**
- `tp1_associativity_go.go` → version **Go**
- `answer_associativity.txt` → résultat Python
- `answer_associativity_llm.txt` → résultat Go
- `Dockerfile`, `shell.nix`, `.github/workflows/run_tp1.yml` → exécution automatisée et reproductible (Docker, Nix, GitHub Actions)

---

## ⚙️ Exécution rapide

### 🐍 Python
```bash
python3 tp1_associativity.py
```

# Go 
```bash
go run tp1_associativity_go.go
```

# Docker
```bash
docker build -t associativity .
docker run --rm -v $(pwd):/usr/src/app/out associativity
```

## Les résultats sont enregistrés dans :
- answer_associativity.txt
- answer_associativity_llm.txt