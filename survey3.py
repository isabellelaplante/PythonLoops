
#survey data
preferences = ["coffee", "tea", "coffee", "soda", "tea","coffee"]

#counting preferences
count = {}

#count each beverage using for loop
for beverage in preferences:
    if beverage in count:
        count[beverage] += 1
    else:
        count[beverage] = 1

    responses = len(preferences)

#calculate and print percentage for each beverage   
for product, count in count.items():
    percentage = (count / responses) * 100
    print(f"{product}: {percentage:.0f}%")


        
