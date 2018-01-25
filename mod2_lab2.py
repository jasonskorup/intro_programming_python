import random

test_num = random.randint(50, 100)
print(test_num)

if test_num % 3 == 0 and test_num % 5 == 0:
    print("fizzbuzz")
elif test_num % 3 == 0:
    print("fizz")
elif test_num % 5 == 0:
    print("buzz")
