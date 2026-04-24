customers = {
    "Alice": 1200, 
    "Bob": 800, 
    "Charlie": 6500,
    "Nick": 3700,
    "Sarah": 5300
}

teirs = {"Bronze": 0, "Silver": 0, "Gold": 0}
for customer, spending in customers.items():
    if spending < 1000:
        teirs["Bronze"] += 1
    elif spending < 5000:
        teirs["Silver"] += 1
    else:
        teirs["Gold"] += 1

for teir, count in teirs.items():
    print(f"{teir}: {count} customers")
    