import streamlit as st  

st.set_page_config(page_title="Time to Distance Converter", layout="centered")  
  
st.title("Convert Time to Distance Driven")  
  
# Create two columns for input and unit selection  
col1, col2 = st.columns(2)  
  
with col1:  
    # Input for time duration without decimal points  
    time_duration = st.number_input("Enter time:", min_value=0, value=2, step=1, format="%d")  
  
with col2:  
    # Select the unit of time  
    unit = st.selectbox("Select unit of time:", ['seconds', 'minutes', 'hours', 'days'], index=1)  
  
# Function to calculate distance based on time and unit  
def calculate_distance(time, unit):  
    # Define speed limits for different time periods  
    if unit == 'seconds':  
        speed = 5 / 3600  # converting to miles per second  
        return time * speed  
    elif unit == 'minutes':  
        if time <= 20:  
            speed = 30 / 60  # converting to miles per minute  
        else:  
            speed = 60 / 60  # converting to miles per minute  
        return time * speed  
    elif unit == 'hours':  
        if time <= 1:  
            speed = 50  
        elif time <= 10:  
            speed = 65  
        else:  
            speed = 70  
        return time * speed  
    elif unit == 'days':  
        speed = 70 * 12  # converting to miles per day (daytime only)  
        return time * speed  
  
# Calculate distance based on input  
distance = calculate_distance(time_duration, unit)  
  
# Inputs for cost calculation  
st.subheader("Cost Calculation")  
  
fuel_type = st.radio("Select vehicle type:", ['Gas', 'Electric'])  
if fuel_type == 'Gas':  
    mpg = st.number_input("Enter miles per gallon (mpg):", min_value=1.0, value=25.0)  
    cost_per_gallon = st.number_input("Enter cost per gallon ($):", min_value=0.0, value=3.0)  
   