FROM python:3.12

WORKDIR /usr/src/app

# Installer Go et Git
RUN apt-get update && apt-get install -y golang git && rm -rf /var/lib/apt/lists/*

# Copier les scripts
COPY tp1_associativity.py ./
COPY tp1_associativity_go.go ./

# Créer un dossier pour les sorties
RUN mkdir -p /usr/src/app/out

# Exécuter les deux tests et copier les résultats à la fin
CMD python3 tp1_associativity.py && \
    go run tp1_associativity_go.go && \
    cp /usr/src/app/*.txt /usr/src/app/out/
