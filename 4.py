try:
    # given user input
    user_input = int(input("Give an integer: "))
    
    # Initialize variables
    total_sum = 0
    current_number = 0
    
    # Calculate the sum using a while loop
    while current_number < user_input:
        total_sum += current_number
        current_number += 1
    
    # Displaying the result
    print(f"The sum was: {total_sum}")
except ValueError:
    print("Please enter a valid integer.")