expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}

grandTotal = 0

#calculate total for each category and grand total
for category, amounts in expenses.items():
  category_total = 0

  for amount in amounts:
    category_total += amount
  
  grandTotal += category_total

 #expense report summary
  print(f"{category}: ${category_total:.2f}")
print(f"\nGrand Total: ${grandTotal:.2f}")

