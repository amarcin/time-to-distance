import streamlit as st

st.title("Convert Time to Distance Driven")

# Selection box
# first argument takes the titleof the selectionbox
# second argument takes options

col1, col2 = st.columns(2)

with col1:
    input = st.number_input("", min_value=0, value=2)

with col2: 
    unit = st.selectbox("",
                     ['minutes', 'hours', 'days'], index=1)

# Equation
# I need to have different classses of time periods. 
# Ex. If the car has been driving between 0 and 20 seconds, it goes x speed 
# 20 sec - 1 min = x speed 
# 1 min - 10 min = x speed
# (freeway) 10 min - 20 min = x speed
# 20+ min

# Thinking, exponentially increasing speed, with a cap at 70 mph

# Ideally, these speeds would be scaling, need to draw it on a graph
output = 0

st.write(output)

if(unit=='seconds'):
    output = input * 5

if (unit=='hours'):
    output = input * 50


if(st.button("Convert")):
    st.write("", output, " miles")

st.header("Conversion")
