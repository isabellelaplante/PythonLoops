initial = float(input("Enter the initial revenue: "))
growth_rate = float(input("Enter the growth rate: "))

# Convert growth rate to a decimal
growth_rate = growth_rate / 100

#for loop to calculate revenue for 10 years
for year in range(1, 11):
    print(f"Year {year}: ${initial:.2f}")
    initial = initial * (1 + growth_rate)



