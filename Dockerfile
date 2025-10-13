FROM python:3.13
WORKDIR /usr/src/app

# Installer git pour permettre un commit/push
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copier le script
COPY tp1_associativity.py ./

# Exécuter le script directement en root
CMD ["python3", "tp1_associativity.py"]
