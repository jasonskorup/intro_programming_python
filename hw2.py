'''
V1 of Homework 2. I'd like to learn how to write some validation around the price input such that users can enter a
string or a float without the script throwing an error. The "without punctuation" prompt is pretty hacky. Otherwise,
the script runs and appears to meet the given requirements.
'''

# Get user's first and last name
print(" ")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

# Get phone number and area code for user ID
area_code = input("What is your zip code? ")
phone = input("What is your phone number? (XXX-XXX-XXXX) ")

# Get car information
make = input("What make of car did you purchase? ")
model = input("What model of car did you purchase? ")
price = float(input("What price did you pay for your car? (Without Punctuation) "))

# Calculate and/or set price outputs
tax = price * 0.10
tax = round(tax, 2)
licensing = 50.00
dealer = 50.00
total_price = price + tax + licensing + dealer

# Convert floats to strings for printing
price = str(price) + "0"
tax = str(tax) + "0"
licensing = str(licensing) + "0"
dealer = str(dealer) + "0"
total_price = str(total_price) + "0"

# Assign the car a unique ID
short_name = last_name[-4:]
short_name = short_name.upper()
user_id = short_name + "_" + area_code

# Print required outputs
print("\n" + "Hello", first_name, last_name, "! \n")
print("Thank you for your purchase of a " + make, model + ". Following is a break down of your total price: \n")
print("Sales Price: $" + price + "\n")
print("Tax: $" + tax + "\n")
print("Licensing Fee: $" + licensing + "\n")
print("Dealer Prep Fee: $" + dealer + "\n")
print("Total Price: $" + total_price + "\n")
print("You have been assigned an ID number of " + user_id + ". Please refer to this ID number if you have")
print("any questions. \n")
