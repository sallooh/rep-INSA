"""
import math

e = math.e

for i in range(50):
    print(e)
    e = e - 1
    e = e * (i+1)

e = e -1
print(e)

"""

# solution de Chat-GPT
import math

# Nombre d'années
n = 50

# Montant initial
montant = math.e  # Utilisation de e exact

# Boucle sur chaque année
for k in range(1, n + 1):
    montant = (montant - 1) * k

# Frais final pour récupérer l'argent
montant -= 1

print("Après", n, "ans, vous aurez environ :", montant)
