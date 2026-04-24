warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]

total_inventory = {}

for warehouse in warehouses:
    for item, amount in warehouse["inventory"].items():
        if item in total_inventory:
            total_inventory[item] += amount
        else:
            total_inventory[item] = amount
    
for item, amount in total_inventory.items():
    print(f"Total {item}: {amount}")    
