import streamlit as st

# Placeholder simulation functions
def simulation_1():
    return "Simulation 1 is running..."

def simulation_2():
    return "Simulation 2 is running..."

def simulation_3():
    return "Simulation 3 is running..."

def simulation_4():
    return "Simulation 4 is running..."

# App title
st.title("Simulation Program Selector")

# Sidebar menu
st.sidebar.title("Choose a Simulation")
selected_simulation = st.sidebar.radio(
    "Select one of the simulations below:",
    ("Simulation 1", "Simulation 2", "Simulation 3", "Simulation 4")
)

# Display selected simulation
if selected_simulation == "Simulation 1":
    st.header("Simulation 1")
    result = simulation_1()
    st.write(result)

elif selected_simulation == "Simulation 2":
    st.header("Simulation 2")
    result = simulation_2()
    st.write(result)

elif selected_simulation == "Simulation 3":
    st.header("Simulation 3")
    result = simulation_3()
    st.write(result)

elif selected_simulation == "Simulation 4":
    st.header("Simulation 4")
    result = simulation_4()
    st.write(result)
