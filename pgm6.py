# A program to check if a number is odd or even
def check_odd_or_even():
    try:
        # Get user input
        number = int(input("Enter a number: "))

        # Check if the number is odd or even
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    except ValueError:
        print("Please enter a valid integer.")

# Run the function
check_odd_or_even()
