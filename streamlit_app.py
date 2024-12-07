import streamlit as st

# Page Navigation
page = st.sidebar.radio(
    "Choose a simulation:",
    ("Simulation 1", "Simulation 2", "Simulation 3", "Simulation 4")
)

# Load and execute the selected simulation
if page == "Simulation 1":
    st.header("Simulation 1")
    from pages.simulation_1 import run_simulation
    result = run_simulation()
    st.write(result)

elif page == "Simulation 2":
    st.header("Simulation 2")
    from pages.simulation_2 import run_simulation
    result = run_simulation()
    st.write(result)

elif page == "Simulation 3":
    st.header("Simulation 3")
    from pages.simulation_3 import run_simulation
    result = run_simulation()
    st.write(result)

elif page == "Simulation 4":
    st.header("Simulation 4")
    from pages.simulation_4 import run_simulation
    result = run_simulation()
    st.write(result)
