import streamlit as st

# App Title and Introduction
st.title("Welcome to the Simulation App")
st.write("""
This app provides various simulations to help you understand different scenarios and processes. 
Use the sidebar to navigate through the simulations.
""")

# Navigation Section
st.sidebar.title("Navigate to Simulations")

# Page Navigation
page = st.sidebar.radio(
    "Select a page:",
    ("Introduction", "Simulations")
)

# Introduction Section
if page == "Introduction":
    st.header("Introduction")
    st.write("""
    This simulation app offers a variety of simulations to help you explore different scenarios and their outcomes. 
    Each simulation is designed to give you insights into specific processes or behaviors. 
    Use the sidebar to choose a simulation and explore it in detail.
    """)

# Simulations Section
elif page == "Simulations":
    st.header("Simulations")
    st.write("""
    Below are the simulations you can explore:
    - **Simulation 1**: Number Guessing Simulation
      - **Description**: A fun game where you guess a random number between 1 and 100. The app gives you hints whether your guess is too high or too low.
      
    - **Simulation 2**: Dynamic ATM Simulation
      - **Description**: Simulates the behavior of an ATM system including transaction processing, account management, and failure handling. This simulation helps you understand how an ATM system operates and responds to various scenarios.
      
    - **Simulation 3**: Analyzing Biased Dice Rolls
      - **Description**: Analyzes the behavior of biased dice rolls to determine if the dice is fair or biased. It simulates multiple rolls and uses statistical methods to provide insights.
      
    - **Simulation 4**: Monte Carlo Dice Simulation
      - **Description**: Uses the Monte Carlo method to simulate and analyze dice rolls over a large number of iterations. It helps in understanding probability distributions and statistical variability.
    """)
