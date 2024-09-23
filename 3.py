# give the user for input
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

# Check if both numbers are even
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
    
# Check if only one of the numbers is even
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("One of the numbers is even.")

else:
    print("Both numbers are odd.")