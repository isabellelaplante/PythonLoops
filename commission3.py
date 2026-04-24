#commission data
sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

def commission(amount):
   return amount * 0.1
   
#calculate commissions for each salesperson
commissions = {}
for salesperson, amount in sales.items():
    commissions[salesperson] = commission(amount)

leaderboard = list(commissions.items())
#sorry for the long code, github was trying to get me to use lamda but we didnt learn that 
# in class so i had to find another way to code the leaderboard without it, i hope this is ok!
for i in range(len(leaderboard)):
    for j in range(i + 1, len(leaderboard)):
        if leaderboard[i][1] < leaderboard[j][1]:
            leaderboard[i], leaderboard[j] = leaderboard[j], leaderboard[i]


for salesperson, commission_amount in leaderboard:
    print(f"{salesperson}: ${commission_amount:.2f}")
