from datetime

def display_current_datetime():
   current_date = datetime.datetime.now()
   print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))
   
display_current_datetime()

def calculate_future_date():
   number_of_days = int(input("Enter the number of days to add to the current date: "))
   future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
<<<<<<< HEAD
   print(f"future date: {future_date}")
=======
   print(f"future date: {future_date.strftime("%Y-%m-%d")}")
>>>>>>> 54cc54779967abcbd33dee1a21342ec5e497ef4d

calculate_future_date()


