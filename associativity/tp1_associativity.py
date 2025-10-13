# tp1_associativity.py
import random

def test_associativity(n=10000):
    """Test how often (x + y) + z == x + (y + z) for random floats."""
    success = 0

    for _ in range(n):
        x = random.uniform(-1e16, 1e16)
        y = random.uniform(-1e16, 1e16)
        z = random.uniform(-1e16, 1e16)

        if (x + y) + z == x + (y + z):
            success += 1

    pourcentage = (success / n) * 100
    return n, success, pourcentage


if __name__ == "__main__":
    n, success, pourcentage = test_associativity()

    print(f"Sur {n} tests :")
    print(f" - Succès exacts : {success}")
    print(f" - Pourcentage de réussite : {pourcentage:.6f}%")

    # Sauvegarde le résultat dans le fichier answer_associativity.txt
    with open("answer_associativity.txt", "w") as f:
        f.write(f"Sur {n} tests :\n")
        f.write(f" - Succès exacts : {success}\n")
        f.write(f" - Pourcentage de réussite : {pourcentage:.6f}%\n")

    print("\nRésultat enregistré dans 'answer_associativity.txt'")
