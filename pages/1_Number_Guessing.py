import random
import matplotlib.pyplot as plt
import time
from collections import deque

# Global variables for storing attempts and guesses
attempts = []
guesses = []

def guess(mode):
    secret_number = random.randint(1, 100000)
    low = 1
    high = 100000
    attempt = 0
    found = False

    while not found:
        # Guess logic for each mode
        if mode == 1:  # Random Guess Mode
            current_guess = random.randint(low, high)
        elif mode == 2:  # Binary Search Mode
            current_guess = (low + high) // 2
        elif mode == 3:  # Ternary Search Mode
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3
            if secret_number < mid1:
                current_guess = low + (mid1 - low) // 2
            elif secret_number > mid2:
                current_guess = high - (high - mid2) // 2
            else:
                current_guess = (mid1 + mid2) // 2
        elif mode == 4:  # Golden Ratio Search Mode
            golden_ratio = 0.618
            mid = int(low + golden_ratio * (high - low))
            current_guess = mid
        elif mode == 5:  # Logarithmic Search Mode
            current_guess = low + int((high - low) / (2 ** (attempt / 10 + 1)))

        # Record data
        attempt += 1
        attempts.append(attempt)
        guesses.append(current_guess)

        # Evaluate guess
        if current_guess == secret_number:
            print(f"Success! Guessed the number {secret_number} in {attempt} attempts!")
            found = True
        elif current_guess < secret_number:
            low = current_guess + 1
        else:
            high = current_guess - 1

        # Plot progress after every 10 attempts
        if attempt % 10 == 0 or found:
            plot_progress(mode, attempt, current_guess, low, high)

def plot_progress(mode, attempt, current_guess, low, high):
    mode_titles = {
        1: 'Random Guess Mode',
        2: 'Binary Search Mode',
        3: 'Ternary Search Mode',
        4: 'Golden Ratio Search Mode',
        5: 'Logarithmic Search Mode'
    }
    title = mode_titles.get(mode, 'Unknown Mode')

    plt.figure(figsize=(10, 5))
    plt.plot(attempts, guesses, 'b-o', label="Guesses")
    plt.axhline(low, color='g', linestyle='--', label="Lower Bound")
    plt.axhline(high, color='r', linestyle='--', label="Upper Bound")
    plt.scatter(attempt, current_guess, color='orange', zorder=5, label=f"Current Guess: {current_guess}")
    plt.xlabel('Attempts')  
    plt.ylabel('Guesses')  
    plt.title(f"{title}\nTotal Attempts: {attempt}")  
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    while True:
        print("Choose the guessing mode:")
        print("1: Random Guess Mode")
        print("2: Binary Search Mode")
        print("3: Ternary Search Mode")
        print("4: Golden Ratio Search Mode")
        print("5: Logarithmic Search Mode")
        print("6: Exit")

        try:
            mode = int(input("Enter the mode (1, 2, 3, 4, 5, or 6): "))
            if mode == 6:
                print("Exiting the simulation. Goodbye!")
                break
            elif mode not in [1, 2, 3, 4, 5]:
                print("Invalid mode selected. Try again.")
            else:
                attempts.clear()
                guesses.clear()
                guess(mode)
        except ValueError:
            print("Invalid input. Please enter a number.")
