FROM python:3.13
WORKDIR /usr/src/app

# Installer git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copier le code
COPY tp1_associativity.py ./

# Créer un utilisateur non-root
RUN useradd app
USER app

# Commande par défaut
CMD ["python3", "tp1_associativity.py"]
