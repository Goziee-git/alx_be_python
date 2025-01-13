from datetime

def display_current_datetime():
   current_date = datetime.datetime.now()
   print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))
   
display_current_datetime()

def calculate_future_date():
   number_of_days = int(input("Enter the number of days to add to the current date: "))
   future_date = datetime.date(2025,1,12) + datetime.timedelta(days=number_of_days)
   print(f"future date: {future_date}")

calculate_future_date()


