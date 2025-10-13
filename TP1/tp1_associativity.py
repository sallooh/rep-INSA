import random

n = 10000  # nombre de répétitions
success = 0  

for _ in range(n):
    x = random.uniform(-1e16, 1e16)
    y = random.uniform(-1e16, 1e16)
    z = random.uniform(-1e16, 1e16)

    if (x + y) + z == x + (y + z):
        success += 1

pourcentage = (success / n) * 100

print(f"Sur {n} tests :")
print(f" - Succès exacts : {success}")
print(f" - Pourcentage de réussite : {pourcentage:.6f}%")
