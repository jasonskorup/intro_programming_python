"""
This is a script that decides what to get on a pizza
"""

# Let the user know what we are asking about
print("What would you like on your pizza:")
# User inputs cheese preference
cheese = input("What type of cheese? ")
# User inputs meat preference
meat = input("What type of meat? ")
# User inputs veggie preference
veggie = input("What type of vegetable? ")

def pizza():
    # Print concatenated response/result
    print("One pizza with " + cheese + ", " + meat + ", and " + veggie + " coming right up!")

pizza()
