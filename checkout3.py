#list of prices for checkout system
prices = []

#while loop to get user input for prices
while True:
    try:
        price = float(input("Enter the price of the item (0 to finish): ")) 
        if price < 0:
          print("Price cannot be negative. Please try again.")
          continue
        if price == 0:
          break
        prices.append(price)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#calculate total, average, and count of items
if prices:
    total = sum(prices)
    count = len(prices)
    average = total / count if count > 0 else 0

    print(f"Total cost: ${total:.2f}")
    print(f"Average price: ${average:.2f}")
    print(f"Number of items: {count}")   
else:
    print("No items added.")