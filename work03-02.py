def get_month_name(month_number):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if 1 <= month_number <= 12:
        return months[sum([month_number]) - 1]
    else:
        return "Invalid month number! Please enter a number between 1 and 12."

try:
    user_input = input("Enter a month number (1-12): ")  
    month_number = int(user_input) 
    month_name = get_month_name(month_number)  
    print(f"The month is: {month_name}") 
except ValueError:
    print("Invalid input! Please enter a valid number.")  
