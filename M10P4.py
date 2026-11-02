def train_ticket(miles):
    if miles >= 30:
        price = 12
    elif miles <= 29:
        price = 10
    elif miles >= 19:
        price = 8
    elif miles >= 10:
        price = 5
    else:
        price = 0
    return price
sum_prices = 0

user_input = input("Do you want to calculate the train ticket price? (yes/no): ")
while user_input.lower() == "yes":
    miles = float(input("Enter the number of miles: "))
    last_name = input("Enter your last name: ")
    price = train_ticket(miles)
    print(f"Train ticket price for {last_name}: ${price:.2f}")
    sum_prices += price
    user_input = input("Do you want to calculate the train ticket price? (yes/no): ")
print(f"Total train ticket prices: ${sum_prices:.2f}")