FROM python:3.13-bullseye

WORKDIR /usr/src/app

# Installer Go, Git et dépendances minimales
RUN apt-get update && \
    apt-get install -y --no-install-recommends golang git && \
    rm -rf /var/lib/apt/lists/*

# Copier les scripts dans le conteneur
COPY tp1_associativity.py ./
COPY tp1_associativity_go.go ./
COPY generate_and_run_all.py ./

# Créer un dossier pour les fichiers de sortie
RUN mkdir -p /usr/src/app/out

# Exécuter Python et Go, puis déplacer les résultats dans /out
CMD python3 tp1_associativity.py && \
    python3 generate_and_run_all.py && \
    go run tp1_associativity_go.go && \
    cp *.txt *.csv /usr/src/app/out/
