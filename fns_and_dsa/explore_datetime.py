from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # print(f"Current Date and Time: {formatted_date}")
    return formatted_date

def calculate_future_date(days_ahead):
    future_date = datetime.datetime.now() + datetime.timedelta(days_ahead)
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    # print(f"Date after {days_ahead} days: {formatted_future_date}")
    return formatted_future_date

print(f"Current date and time: {display_current_datetime()}")

input_days = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date(input_days)}")