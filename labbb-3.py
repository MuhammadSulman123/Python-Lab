
# LAB 3 | Python Programming Exercises
# ---------------------------------------------------------------------------
# Exercise 1
# Find numbers divisible by 7 and also multiples of 5 from 1500 to 2700.
# ---------------------------------------------------------------------------

def exercise_1():
    print_header("EXERCISE 1 | Numbers divisible by 7 and 5")

    results = [
        number
        for number in range(1500, 2701)
        if number % 7 == 0 and number % 5 == 0
    ]

    print("Numbers from 1500 to 2700 that are divisible by both 7 and 5:")
    print(", ".join(map(str, results)))


# ---------------------------------------------------------------------------
# Exercise 2
# Convert temperatures between Celsius and Fahrenheit.
# Formula: C / 5 = (F - 32) / 9
# ---------------------------------------------------------------------------

def exercise_2():
    print_header("EXERCISE 2 | Temperature converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose conversion (1 or 2): ").strip()

    if choice not in {"1", "2"}:
        print("Please choose 1 or 2.")
        return

    try:
        temperature = float(input("Enter the temperature: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == "1":
        converted = (temperature * 9 / 5) + 32
        print(f"\n{temperature:g}Â°C = {converted:.2f}Â°F")
    else:
        converted = (temperature - 32) * 5 / 9
        print(f"\n{temperature:g}Â°F = {converted:.2f}Â°C")


# ---------------------------------------------------------------------------
# Exercise 3
# Keep asking the user to guess a number from 1 to 9 until it is correct.
# ---------------------------------------------------------------------------

def exercise_3():
    print_header("EXERCISE 3 | Guess the number")
    secret_number = random.randint(1, 9)
    attempts = 0

    print("I have chosen a number between 1 and 9.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 9:
            print("Your number must be between 1 and 9.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Well guessed! You got it in {attempts} attempt(s).")
            break

        print("Not quite. Try again!")


# ---------------------------------------------------------------------------
# Exercise 4
# Print the required star pattern using nested loops.
# ---------------------------------------------------------------------------

def exercise_4():
    print_header("EXERCISE 4 | Star pattern")
    row_widths = list(range(1, 6)) + list(range(4, 0, -1))

    for width in row_widths:
        for _ in range(width):
            print("*", end=" ")
        print()


# ---------------------------------------------------------------------------
# Exercise 5
# Accept a word and display it in reverse.
# ---------------------------------------------------------------------------

def exercise_5():
    print_header("EXERCISE 5 | Reverse a word")
    word = input("Enter a word: ")
    print(f"Reversed word: {word[::-1]}")


# ---------------------------------------------------------------------------
# Exercise 6
# Count even and odd values in a series of numbers.
# ---------------------------------------------------------------------------

def exercise_6():
    print_header("EXERCISE 6 | Count even and odd numbers")
    print("Enter numbers separated by commas.")
    print("Example: 1, 2, 3, 4, 5, 6, 7, 8, 9")
    raw_values = input("Numbers: ").strip()

    if not raw_values:
        numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        print("Using the sample numbers:", numbers)
    else:
        try:
            numbers = tuple(int(value.strip()) for value in raw_values.split(","))
        except ValueError:
            print("Invalid input. Please enter whole numbers separated by commas.")
            return

    even_count = sum(number % 2 == 0 for number in numbers)
    odd_count = sum(number % 2 != 0 for number in numbers)

    print(f"\nEven numbers: {even_count}")
    print(f"Odd numbers:  {odd_count}")


# ---------------------------------------------------------------------------
# Exercise 7
# Print every item in the given list and its data type.
# ---------------------------------------------------------------------------

def exercise_7():
    print_header("EXERCISE 7 | List items and their data types")

    data = [
        1452,
        11.23,
        1 + 2j,
        True,
        "w3resource",
        (0, -1),
        [5, 12],
        {"class": "V", "section": "A"},
    ]

    for index, item in enumerate(data, start=1):
        print(f"{index:>2}. Value: {item!r}")
        print(f"    Type:  {type(item).__name__}")


# ---------------------------------------------------------------------------
# Exercise 8
# Print numbers 0 through 6, skipping 3 and 6 with continue.
# ---------------------------------------------------------------------------

def exercise_8():
    print_header("EXERCISE 8 | Using continue")

    for number in range(7):
        if number in (3, 6):
            continue
        print(number, end=" ")
    print()


# ---------------------------------------------------------------------------
# Exercise 9
# Display Fibonacci numbers between 0 and 50.
# ---------------------------------------------------------------------------

def exercise_9():
    print_header("EXERCISE 9 | Fibonacci series (0 to 50)")

    first, second = 0, 1
    fibonacci_numbers = []

    while first <= 50:
        fibonacci_numbers.append(first)
        first, second = second, first + second

    print(" ".join(map(str, fibonacci_numbers)))


# ---------------------------------------------------------------------------
# Exercise 10
# Print a 2D array where each element is row_index * column_index.
# Both indexes begin at 0.
# ---------------------------------------------------------------------------

def exercise_10():
    print_header("EXERCISE 10 | Generate a 2D multiplication array")

    try:
        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns: "))
    except ValueError:
        print("Please enter whole numbers.")
        return

    if rows <= 0 or columns <= 0:
        print("Rows and columns must both be greater than zero.")
        return

    matrix = [
        [row_index * column_index for column_index in range(columns)]
        for row_index in range(rows)
    ]

    print("\nGenerated array:")
    for row in matrix:
        print(row)


# ---------------------------------------------------------------------------
# Exercise 11
# Read lines until a blank line is entered, then print them in lowercase.
# ---------------------------------------------------------------------------

def exercise_11():
    print_header("EXERCISE 11 | Convert input lines to lowercase")
    print("Type your lines below. Press Enter on an empty line to finish.")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.lower())

    print("\nLowercase output:")
    if lines:
        print("\n".join(lines))
    else:
        print("(No lines were entered.)")


# ---------------------------------------------------------------------------
# Exercise 12
# From comma-separated 4-digit binary values, print those divisible by 5.
# ---------------------------------------------------------------------------

def exercise_12():
    print_header("EXERCISE 12 | Binary numbers divisible by 5")
    raw_values = input(
        "Enter 4-digit binary numbers separated by commas: "
    ).strip()

    if not raw_values:
        print("No numbers entered.")
        return

    binary_values = [value.strip() for value in raw_values.split(",")]
    valid_values = []

    for value in binary_values:
        if len(value) != 4 or any(bit not in "01" for bit in value):
            print(f"Skipping invalid 4-digit binary value: {value!r}")
            continue

        if int(value, 2) % 5 == 0:
            valid_values.append(value)

    print("\nMatching binary numbers:")
    print(",".join(valid_values) if valid_values else "None")


# ---------------------------------------------------------------------------
# Exercise 13
# Count letters and digits in a string.
# ---------------------------------------------------------------------------

def exercise_13():
    print_header("EXERCISE 13 | Count letters and digits")
    text = input("Enter a string: ")

    letter_count = sum(character.isalpha() for character in text)
    digit_count = sum(character.isdigit() for character in text)

    print(f"\nLetters: {letter_count}")
    print(f"Digits:  {digit_count}")


# ---------------------------------------------------------------------------
# Exercise 14
# Validate a password using the requirements in the Lab 3 sheet:
# - At least one lowercase and one uppercase letter
# - At least one digit
# - At least one special character from $, #, @
# - Length from 6 to 16 characters
# ---------------------------------------------------------------------------

def is_valid_password(password):
    """Return True when the password meets every lab requirement."""
    has_lowercase = any(character in string.ascii_lowercase for character in password)
    has_uppercase = any(character in string.ascii_uppercase for character in password)
    has_digit = any(character in string.digits for character in password)
    has_special = any(character in "$#@" for character in password)
    valid_length = 6 <= len(password) <= 16

    return (
        has_lowercase
        and has_uppercase
        and has_digit
        and has_special
        and valid_length
    )


def exercise_14():
    print_header("EXERCISE 14 | Password validation")
    print("Password requirements:")
    print("  â€¢ 6 to 16 characters")
    print("  â€¢ At least one lowercase letter (a-z)")
    print("  â€¢ At least one uppercase letter (A-Z)")
    print("  â€¢ At least one digit (0-9)")
    print("  â€¢ At least one special character from: $, #, @")

    password = input("\nEnter a password to check: ")

    if is_valid_password(password):
        print("Valid password. All requirements are met.")
    else:
        print("Invalid password. Please check the requirements above.")


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

EXERCISES = {
    "1": exercise_1,
    "2": exercise_2,
    "3": exercise_3,
    "4": exercise_4,
    "5": exercise_5,
    "6": exercise_6,
    "7": exercise_7,
    "8": exercise_8,
    "9": exercise_9,
    "10": exercise_10,
    "11": exercise_11,
    "12": exercise_12,
    "13": exercise_13,
    "14": exercise_14,
}


def show_menu():
    """Display the list of available lab exercises."""
    print("\n" + "â•”" + "â•" * 66 + "â•—")
    print("â•‘" + " " * 22 + "PYTHON LAB 3" + " " * 32 + "â•‘")
    print("â• " + "â•" * 66 + "â•£")
    exercise_names = [
        "Divisible by 7 and 5",
        "Temperature converter",
        "Guess the number",
        "Star pattern",
        "Reverse a word",
        "Count even and odd numbers",
        "List items and data types",
        "Using continue",
        "Fibonacci series",
        "Generate a 2D array",
        "Lowercase input lines",
        "Binary numbers divisible by 5",
        "Count letters and digits",
        "Password validation",
    ]

    for number, name in enumerate(exercise_names, start=1):
        print(f"â•‘  {number:>2}. {name:<59}â•‘")

    print("â• " + "â•" * 66 + "â•£")
    print("â•‘  0. Exit" + " " * 57 + "â•‘")
    print("â•š" + "â•" * 66 + "â•")


def main():
    """Run the menu until the user chooses to exit."""
    while True:
        show_menu()
        choice = input("\nSelect an exercise (0-14): ").strip()

        if choice == "0":
            print("\nThank you for using Python Lab 3. Goodbye!")
            break

        exercise = EXERCISES.get(choice)
        if exercise is None:
            print("Invalid choice. Please select a number from 0 to 14.")
            continue

        exercise()
        pause()


if __name__ == "__main__":
    main()