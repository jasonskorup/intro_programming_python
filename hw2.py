'''
Gather the following user input and store each item as a variable:
Purchaser name
Purchaser address
Purchaser phone number (entered as 503-555-1211)
Car Make/Model
Purchase Price
'''

# Get user's first and last name
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

# Get phone number and area code for user ID
area_code = input("What is your zip code? ")
phone = input("What is your phone number? (XXX-XXX-XXXX) ")

# Get car information
make = input("What make of car did you purchase? ")
model = input("What model of car did you purchase? ")
price = float(input("What price did you pay for your car? "))

# Calculate and/or set price outputs
tax = price * 0.10
tax = round(tax, 2)
licensing = 50.00
dealer = 50.00
total_price = price + tax + licensing + dealer

# Convert floats to strings for printing
price = str(price)
tax = str(tax)
licensing = str(licensing)
dealer = str(dealer)
total_price = str(total_price)

# Assign the car a unique ID
short_name = last_name[-4:]
short_name.upper()
user_id = short_name + "_" + area_code

# Print required outputs
print("Hello" + first_name + last_name + "! \n")
print("Thank you for your purchase of a " + make + model + ". Following is a break down of your total price:")
print("Sales Price: " + price)
print("Tax: " + tax)
print("Licensing Fee: " + licensing)
print("Dealer Prep Fee: " + dealer)
print("Total Price: " + total_price)
print("You have been assigned an ID number of " + user_id + ". Please refer to this ID number if you have")
print("any questions.")
