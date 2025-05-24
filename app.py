import streamlit as st
from api_client import get_current_weather, get_next_days_weather

css = """
.st-emotion-cache-1w723zb {
    max-width: 1250px;
}
"""

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title("Weather Tracker :earth_asia:")

city = st.text_input(label="City:red[*]", placeholder='New York', value="")

days = st.number_input(label="Days forecast you want to search", min_value=0, max_value=3, placeholder=0, help="Let days as 0 if you want to check the weather for today!", value=0)

if st.button(label="Check Weather"):
    if city != "" and days == 0:
        response = get_current_weather(city)
        st.write(response)
    elif city != "" and days > 0:
        response = get_next_days_weather(city, days)
        st.write(response)
    else:
        st.warning("You must fill at least the city field!")