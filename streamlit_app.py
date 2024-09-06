import streamlit as st  
  
st.title("Convert Time to Distance Driven")  
  
# Create two columns for input and unit selection  
col1, col2 = st.columns(2)  
  
with col1:  
    # Input for time duration  
    time_duration = st.number_input("Enter time:", min_value=0.0, value=2.0)  
  
with col2:  
    # Select the unit of time  
    unit = st.selectbox("Select unit of time:", ['seconds', 'minutes', 'hours', 'days'], index=1)  
  
# Function to calculate distance based on time and unit  
def calculate_distance(time, unit):  
    # Define speed limits for different time periods  
    if unit == 'seconds':  
        # Assuming speed is constant at 5 mph for simplicity  
        speed = 5 / 3600  # converting to miles per second  
        return time * speed  
    elif unit == 'minutes':  
        # 0-20 minutes: 30 mph, 20+ minutes: 60 mph  
        if time <= 20:  
            speed = 30 / 60  # converting to miles per minute  
        else:  
            speed = 60 / 60  # converting to miles per minute  
        return time * speed  
    elif unit == 'hours':  
        # 0-1 hour: 50 mph, 1-10 hours: 65 mph, 10+ hours: 70 mph  
        if time <= 1:  
            speed = 50  
        elif time <= 10:  
            speed = 65  
        else:  
            speed = 70  
        return time * speed  
    elif unit == 'days':  
        # Assuming constant speed of 70 mph  
        speed = 70 * 24  # converting to miles per day  
        return time * speed  
  
# Calculate distance based on input  
distance = calculate_distance(time_duration, unit)  
  
# Button to trigger conversion  
if st.button("Convert"):  
    st.write(f"Distance Driven: {distance:.2f} miles")  
  
st.header("Conversion")  