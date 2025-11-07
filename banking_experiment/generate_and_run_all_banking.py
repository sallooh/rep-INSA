# generate_and_run_all_banking.py
import random
import csv
import math
from itertools import product
from decimal import Decimal, getcontext

# Define variability factors
factors_options = {
    "initial_money": [math.e, 3.0, 10.0],
    "years": [10, 20, 50],
    "fee": [1.0, 0.5, 2.0],
    "stochastic_fee": [False, True],
    "seed": [None, 42],
    "precision": ["float", "decimal"]
}

def banking_simulation(initial_money=2.71828, years=50, fee=1.0, stochastic_fee=False,
                       seed=None, precision="float"):
    """Simulate the banking process and return final money."""
    if seed is not None:
        random.seed(seed)

    if precision == "decimal":
        getcontext().prec = 50
        money = Decimal(str(initial_money))
        fee = Decimal(str(fee))
    else:
        money = float(initial_money)

    for i in range(1, years + 1):
        current_fee = fee
        if stochastic_fee:
            fluct = random.uniform(-0.1, 0.1)  # random variation of ±0.1 euro
            current_fee = fee + (Decimal(str(fluct)) if precision == "decimal" else fluct)

        money = (money - current_fee) * i

    money -= (Decimal(1) if precision == "decimal" else 1.0)
    return float(money)  # convert back to float for consistency in CSV

# Run all combinations
keys, values = zip(*factors_options.items())
results = []

for combination in product(*values):
    params = dict(zip(keys, combination))
    final_money = banking_simulation(**params)
    results.append({**params, "final_money": final_money})
    print(f"Run with {params} -> final money: {final_money:.6e}")

# Save to CSV
with open("variability_results_banking.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list(factors_options.keys()) + ["final_money"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("\nResults saved to 'variability_results_banking.csv'")
