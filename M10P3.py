def out_the_door(msrp, make, model, electric_code):
    if make.lower() == "honda" and model.lower() == "accord":
        discount_price = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        discount_price = 0.15
    elif electric_code.upper() == "YES":
        discount_price = 0.30
    else:
        discount_price = 0
    
    discount = msrp * discount_price
    new_msrp = msrp - discount
    tax = new_msrp * 0.07
    total = new_msrp + tax
    return total
total_sales_price = 0
total_msrp = 0
user_input = input("Do you want to calculate the out-the-door price? (yes/no): ")
while user_input.lower() == "yes":
    msrp = float(input("Enter the MSRP: "))
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    electric_code = input("Is it an electric vehicle? (yes/no): ")
    total = out_the_door(msrp, make, model, electric_code)
    total_sales_price += total
    total_msrp += msrp
    print(f"Out-the-door price: ${total:.2f}")
    user_input = input("Do you want to calculate the out-the-door price? (yes/no): ")
print(f"Total sales price: ${total_sales_price:.2f}")
print(f"Total MSRP: ${total_msrp:.2f}")
print(f"Total discount: ${total_msrp - total_sales_price:.2f}")