import streamlit as st
from api_client import get_current_weather, get_next_days_weather
from database import check_if_exists, insert_to_SQL
import pandas as pd
from datetime import date
import datetime

css = """s
.st-emotion-cache-1w723zb {
    max-width: 1250px;
}
"""

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

@st.dialog("Current Weather")
def show_current_weather(city, temperature, sensation, humidity, condition, condition_icon):
    col1, col2 = st.columns(2)
    with col1:
        st.write(" ")
        st.subheader(f"Weather in {city}:")
    with col2:
        st.image(f"https:{condition_icon}")
    st.write(f"Temperature: {temperature}")
    st.write(f"Feels like: {sensation}")
    st.write(f"Humidity: {humidity}")
    st.write(f"Condition: {condition}")

@st.dialog(f"Forecast")
def show_forecast_weather(city, days_list):
    count = 0
    st.header(f"Weather in {city}:")
    for day in days_list:
        st.subheader(f"{day["current_date"]}:")
        st.write(f"Max Temperature: {day["max_temp"]}")
        st.write(f"Min Temperature: {day["min_temp"]}")
        st.write(f"Condition: {day["condition"]}")
        st.image(f"https:{day["condition_icon"]}")
        if count < len(days_list)-1:
            st.write("------")
        count += 1  

st.title("Weather Tracker :earth_asia:")

city = st.text_input(label="City:red[*]", placeholder='New York', value="")

days = st.number_input(label="Days forecast you want to search", min_value=0, max_value=3, placeholder=0, help="Let days as 0 if you want to check the weather for today!", value=0)

if st.button(label="Check Weather"):
    current_date = datetime.date.today()
    
    if city != "" and days == 0:
        query_result = check_if_exists(city, current_date) 

        if query_result == []:
            response = get_current_weather(city)

            current_date = response["location"]["localtime"].split()[0]
            temperature = response["current"]["temp_c"]
            sensation = response["current"]["feelslike_c"]
            humidity = response["current"]["humidity"]
            condition = response["current"]["condition"]["text"]
            condition_icon = response["current"]["condition"]["icon"]
            
            check = insert_to_SQL(city=city, current_date=current_date, temperature=temperature, sensation=sensation, humidity=humidity, condition=condition, condition_icon=condition_icon)
            
            print(f"Inserted on Database: {check}")
        
        else:
            print("Already exists on Database")
            
            current_date = query_result[0][2]
            temperature = query_result[0][3]
            sensation = query_result[0][4]
            humidity = query_result[0][5]
            condition = query_result[0][6]
            condition_icon = query_result[0][7]

        show_current_weather(city, temperature, sensation, humidity, condition, condition_icon)
        
    elif city != "" and days > 0:
        data = []
        query_result = check_if_exists(city, current_date, days)
        st.write(query_result)

        if query_result == []:
            response = get_next_days_weather(city, days)

            for day in response["forecast"]["forecastday"]:
                current_date = day["date"]
                max_temp = day["day"]["maxtemp_c"]
                min_temp = day["day"]["mintemp_c"]
                condition = day["day"]["condition"]["text"]
                condition_icon = day["day"]["condition"]["icon"]
                data.append({"current_date": current_date,
                            "max_temp":max_temp, 
                            "min_temp":min_temp,
                            "condition":condition,
                            "condition_icon":condition_icon})

                check = insert_to_SQL(city=city, current_date=current_date, condition=condition, condition_icon=condition_icon, days=days, max_temp=max_temp, min_temp=min_temp)
                print(f"Inserted on Database: {check}")
        else:
            print("Already exists on Database")
            
            for day in query_result:
                data.append({"current_date": day[2],
                            "max_temp":day[5], 
                            "min_temp":day[6],
                            "condition":day[3],
                            "condition_icon":day[4]})
            
        show_forecast_weather(city, data)

    else:
        st.warning("You must fill at least the city field!")