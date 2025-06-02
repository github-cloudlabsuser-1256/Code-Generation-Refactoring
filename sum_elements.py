# A refactored version of the Python program that prompts the user for the number of elements to sum, takes those integers as input, and handles basic error cases

MAX = 100

def get_number_of_elements():
    while True:
        try:
            n = int(input(f"Enter the number of elements (1-{MAX}): "))
            if 1 <= n <= MAX:
                return n
            else:
                print(f"Invalid input. Please provide a number between 1 and {MAX}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_integer_inputs(n):
    arr = []
    print(f"Enter {n} integers:")
    while len(arr) < n:
        try:
            value = int(input(f"Element {len(arr)+1}: "))
            arr.append(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return arr

def calculate_sum(arr):
    return sum(arr)

def main():
    try:
        n = get_number_of_elements()
        arr = get_integer_inputs(n)
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
