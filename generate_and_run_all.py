# generate_and_run_all.py
import random
import csv
from itertools import product

# Définition des facteurs et de leurs valeurs possibles
factors_options = {
    "seed": [None, 42, 123],
    "n": [1000, 10000],
    "range_max": [1e8, 1e16]
}

# Fonction de test qui prend les facteurs comme paramètres
def test_property(n=10000, seed=None, range_max=1e16):
    if seed is not None:
        random.seed(seed)
    success = 0
    for _ in range(n):
        x = random.uniform(-range_max, range_max)
        y = random.uniform(-range_max, range_max)
        z = random.uniform(-range_max, range_max)
        if (x + y) + z == x + (y + z):
            success += 1
    percent = (success / n) * 100
    return n, success, percent

# Boucle sur toutes les combinaisons
keys, values = zip(*factors_options.items())
results = []

for combination in product(*values):
    params = dict(zip(keys, combination))
    n, success, percent = test_property(**params)
    results.append({**params, "success": success, "percent": percent})
    print(f"Run with {params} -> {percent:.6f}% success")

# Sauvegarde des résultats dans un CSV
with open("variability_results.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list(factors_options.keys()) + ["success", "percent"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("\nResults saved to 'variability_results.csv'")
