import streamlit as st

st.title("Convert Time to Distance Driven")

# Selection box
# first argument takes the titleof the selectionbox
# second argument takes options

input = st.number_input("", min_value=0, value=2)

unit = st.selectbox("",
                     ['seconds', 'minutes', 'hours', 'days'], index=2)

# Equation

# I need to have different classses of time periods. 
# Ex. If the car has been driving between 0 and 20 seconds, it goes x speed 
# 20 sec - 1 min = x speed 
# 1 min - 10 min = x speed
# (freeway) 10 min - 20 min = x speed
# 20+ min

# Ideally, these speeds would be scaling, need to draw it on a graph
ouput = 0

if(unit=='seconds'):
    output = input * 5


if(st.button("Convert")):
    st.write("", output, unit)

st.header("Conversion")
