from datetime import datetime

# testing the output of this
today = str(datetime.now().date())
print(today)

# testing out to concatenate our user date input 
month = "January"
month_number_full = datetime.strptime(month, "%B").month
print(f"The month number for '{month}' is: {month_number_full}")

today = str(datetime.now().date().year)
print(today)

x = datetime(2020, month_number_full, 17)

print(x)