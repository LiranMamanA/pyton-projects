import pandas as pd
from collections import Counter
import random
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
def analyze_and_generate_lottery_numbers(file_path):
    # Read the Excel/CSV file
    data = pd.read_csv(file_path)  # Use pd.read_excel(file_path) for Excel files

    # Get all lottery numbers from the data
    all_numbers = data.iloc[:, :6].values.flatten()

    # Count the occurrences of each number
    number_counts = Counter(all_numbers)

    # Find the most common numbers
    most_common_numbers = number_counts.most_common()

    print("Most common lottery numbers:")
    for number, count in most_common_numbers:
        print(f"Number: {number}, Occurrences: {count}")

    # Choose a strong number from the same file
    strong_number = data['Strong Number'].values[0]  # Replace 'Strong Number' with the actual column name
    print(f"\nChosen strong number: {strong_number}")

    # Generate 6 random lottery numbers between 1 and 37 for the future
    future_random_numbers = random.sample(range(1, 38), 6)
    print("\nGenerated random lottery numbers for the future:")
    print(", ".join(map(str, future_random_numbers)))

    # Generate a random strong number between 1 and 7 for the future
    future_random_strong_number = random.randint(1, 7)
    print(f"Generated random strong number for the future: {future_random_strong_number}")

# Replace 'your_file_path.csv' with the path to your CSV file
analyze_and_generate_lottery_numbers('C:\Lottery\Lotto.csv')
