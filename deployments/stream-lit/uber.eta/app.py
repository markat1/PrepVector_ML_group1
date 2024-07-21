import streamlit as st
from helpers.haversine import calc_dist_with_haversine

st.header("Calculate amount of time it takes to deliver food")

st.text_input("Distance", key="distance", value=1000)

distance = st.session_state.distance

chosen_vehicle = st.selectbox(
    'Choose vehicle',
     ['scooter','electric_scooter','motorcycle'])

vehicle_condition = st.selectbox(
    'Choose vehicle condition',
     [1,2])

weather_condition = st.selectbox(
    'Choose weather condition',
     ['conditions Sunny', 'conditions Windy', 'conditions Stormy', 'conditions Cloudy','conditions Fog'])

traffic_condition = st.selectbox(
    'Choose traffic',
     ['Low','Medium','High', 'Jam'])

if st.button("Submit",type="primary"):
    st.write("Test")
