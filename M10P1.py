def forecast_sales(last_name, month, sales):
    if month == "January" or month == "February" or month == "March":
        forecast_percent = 0.10
    elif month == "April" or month == "May" or month == "June":
        forecast_percent = 0.15
    elif month == "July" or month == "August" or month == "September":
        forecast_percent = 0.20
    elif month == "October" or month == "November" or month == "December":
        forecast_percent = 0.25
    else:
        forecast_percent = 0.00

    next_month = sales * (1 + forecast_percent)

    num_data += 1

    print(f"Last Name: {last_name}")
    print(f"Month: {month}")
    print(f"Sales Amount: ${sales:.2f}")
    print(f"Forecast Percent: {forecast_percent:.2%}")
    print(f"Next Month: ${next_month:.2f}")

    return next_month

user_input = input("Do you want to do this program? (yes/no): ")

while user_input.lower() == "yes":
    last_name = input("Enter your last name: ")
    month = input("Enter the month: ")
    sales = float(input("Enter the sales amount: "))

    def forecast_sales(month, sales):
        if month.lower() in ["january", "february", "march"]:
            forecast_percent = 0.10
        elif month.lower() in ["april", "may", "june"]:
            forecast_percent = 0.15
        elif month.lower() in ["july", "august", "september"]:
            forecast_percent = 0.20
        elif month.lower() in ["october", "november", "december"]:
            forecast_percent = 0.25
        else:
            forecast_percent = 0.00

        next_month = sales * (1 + forecast_percent)
        return next_month, forecast_percent

    next_month, forecast_percent = forecast_sales(month, sales)

    print(f"Last Name: {last_name}")
    print(f"Month: {month}")
    print(f"Sales Amount: ${sales:.2f}")
    print(f"Forecast Percent: {forecast_percent:.2%}")
    print(f"Next Month's Sales: ${next_month:.2f}")

    user_input = input("Do you want to do this program again? (yes/no): ")


