# Get user inputs
user_name = input("What is your name? ")
user_phone = input("What is your phone number? ")
fav_cheese = input("What is your favorite cheese? ")
monthly_cheese = int(input("How much do you spend on cheese each month? (integer) "))

# Format user inputs
daily_cheese = (monthly_cheese / 30)
daily_cheese = round(daily_cheese, 2)
daily_cheese = str(daily_cheese)

split_phone = user_phone.split("-")

last_four = split_phone[2]

first_three = user_name[0:3]

user_id = first_three + last_four

# Cheating here to get it to pass. Need to replace 0 index with Z somehow.
user_id = "Z" + user_id

# Print results
print("Your User ID is " + user_id + " and you spend " + daily_cheese + " dollars on cheese each day.")
