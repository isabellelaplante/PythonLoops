import random
#stocks and prices 
portfolio = {
    "GOOGL": {"shares": 15, "price": 350},
    "MSFT": {"shares": 10, "price": 145},
    "AMZN": {"shares": 5, "price": 120}
}

Value = 0
#for loop to calculate total value of the portfolio
for stock, data in portfolio.items():
    stock_value = data["shares"] * data["price"]
    Value += stock_value
print(f"Total Portfolio Value: ${Value:.2f}")

#random price changes
#for loop to simulate price changes over 5 days
for day in range(1, 6):
    for stock, data in portfolio.items():
        change = random.uniform(-0.05, 0.05)
        data["price"] *= (1 + change)

#calculate daily portfolio value
    daily_value = 0
    for stock, data in portfolio.items():
        daily_value += data["shares"] * data["price"]
        
    print(f"Day {day}: Portfolio Value: ${daily_value:.2f}")


