# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
birth = int(input("Enter your year of birth: "))

# Extract components for password
last_two_digits = str(birth)[-2:] 
first_three_letters = name[:3]  
age_squared = str(age ** 2)  

# Generate the password
password = last_two_digits + first_three_letters + age_squared

# Print the password
print("Your password is:", password)