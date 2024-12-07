import random
import time
import matplotlib.pyplot as plt
import streamlit as st
from collections import deque

# Colors and Simulation Data Storage
attempts = deque(maxlen=1000)  # Limit max attempts for better performance
guesses = deque(maxlen=1000)

# Define Guessing Function
def guess(mode, secret_number):
    """Run the guessing simulation in the selected mode."""
    low = 1
    high = 100000
    attempt = 0
    found = False
    st.session_state.progress_bar = st.progress(0)
    
    while not found:
        # Guess logic
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
        
        # Update Progress
        progress = min(attempt / 1000, 1.0)
        st.session_state.progress_bar.progress(progress)
        
        # Evaluate guess
        if current_guess == secret_number:
            found = True
            st.success(f"Success! Guessed the number {secret_number} in {attempt} attempts!")
        elif current_guess < secret_number:
            low = current_guess + 1
        else:
            high = current_guess - 1
        
        # Plot Progress
        plot_progress(mode, attempt, current_guess, low, high)

def plot_progress(mode, attempt, current_guess, low, high):
    """Plot progress dynamically in Streamlit."""
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
    st.pyplot(plt)

# Streamlit App
st.title("Number Guessing Simulation")
st.sidebar.header("Configuration")

# Sidebar Inputs
mode = st.sidebar.selectbox(
    "Choose Guessing Mode",
    [1, 2, 3, 4, 5],
    format_func=lambda x: {
        1: 'Random Guess Mode',
        2: 'Binary Search Mode',
        3: 'Ternary Search Mode',
        4: 'Golden Ratio Search Mode',
        5: 'Logarithmic Search Mode'
    }[x]
)
start_simulation = st.sidebar.button("Start Simulation")

# Main Area
if start_simulation:
    st.write(f"Running simulation in **{mode}** mode...")
    attempts.clear()
    guesses.clear()
    secret_number = random.randint(1, 100000)
    guess(mode, secret_number)
