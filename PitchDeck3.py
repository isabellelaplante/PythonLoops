#random data for pitch deck
revenues = [10, 20, 30, 40, 50]

for i in range(len(revenues)):
    bar = "#" * (revenues[i] // 10)
    print(f"Revenue {i + 1}: {bar} (${revenues[i]})")

