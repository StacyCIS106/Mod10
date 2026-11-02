def assessed_value(county, market_value):
    if county == "Cook":
        assessed = market_value * 0.90
    elif county == "DuPage":
        assessed = market_value * 0.80
    elif county == "McHenry":
        assessed = market_value * 0.75
    elif county == "Kane":
        assessed = market_value * 0.65
    return assessed

total_assessed = 0
user_input = input("Do you want to calculate the assessed value? (yes/no): ")
while user_input.lower() == "yes":
    county = input("Enter the county: ")
    market_value = float(input("Enter the market value: "))
    assessed = assessed_value(county, market_value)
    total_assessed += assessed
    print(f"Assessed value for {county}: ${assessed:.2f}")
    user_input = input("Do you want to calculate the assessed value? (yes/no): ")
print(f"Total assessed value: ${total_assessed:.2f}")