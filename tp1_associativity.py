# tp1_associativity_range.py
import random

def test_associativity(n=10000, value_range=(-1e16, 1e16)):
    """Test how often (x + y) + z == x + (y + z) for random floats in a given range."""
    success = 0
    a, b = value_range

    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(a, b)
        z = random.uniform(a, b)

        if (x + y) + z == x + (y + z):
            success += 1

    pourcentage = (success / n) * 100
    return success, pourcentage


if __name__ == "__main__":
    n = 100000
    ranges = [
        (-1e0, 1e0),
        (-1e3, 1e3),
        (-1e6, 1e6),
        (-1e9, 1e9),
        (-1e12, 1e12),
        (-1e16, 1e16)
    ]

    results = []

    print(f"Testing associativity over {n} random triples per range...\n")

    for r in ranges:
        success, percent = test_associativity(n, r)
        results.append((r, success, percent))
        print(f"Range {r[0]:.0e} to {r[1]:.0e} -> {percent:.6f}% equal results")

    # Save to file
    with open("answer_associativity.txt", "w") as f:
        f.write(f"Results for {n} tests per range:\n\n")
        for (r, success, percent) in results:
            f.write(f"Range {r[0]:.0e} to {r[1]:.0e}:\n")
            f.write(f"  - Exact matches: {success}\n")
            f.write(f"  - Percentage: {percent:.6f}%\n\n")

    print("\nResults saved to 'answer_associativity.txt'")
