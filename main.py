import streamlit as st
import datetime

st.title("Food App",text_alignment="center")
name = st.text_input("Enter your Name")
city = st.selectbox(
    "Select your City",
    ["Ahmedabad", "Surat", "Mumbai", "Delhi", "Bangalore"]
)
food = st.multiselect(
    "Select your Food Preference",
    ["Ittalian", "kathyawadi", "Fast Food", "Punjabi", "Gujarati"]
)
order_count = st.slider(
    "How many times have you ordered?",
    min_value=1,
    max_value=99,
    value=1
)

Gender = st.radio("Choose your Gender",["Male","Female"])
DOB = st.date_input("Choose your DOB")

c1,c2 = st.columns(2)
food_items = c1.multiselect(
    "Food Items",
    ["Pizza", "Sandwich", "Samosa", "Panipuri", "Dosa"]
)
beverages = c2.multiselect(
    "Beverages",
    ["Coco cola", "Fanta", "7up", "Sprite"]
)
Audio = st.audio_input("Record your foods items and beverages you want.")

feedback = st.text_area("Give your feedback")
agreements = st.checkbox("I agree")


if st.button("Submit", type="primary"):
    st.success("Order Submitted Successfully!")

    st.write("## Order Details")
    st.write(f"Name: {name}")
    st.write(f"City: {city}")
    st.write(f"Food Selected: {', '.join(food)}")
    st.write(f"Ordered: {order_count} times")
    st.write(f"Gender: {Gender}")
    st.write(f"DOB: {DOB}")
    st.write("Food Items:", food_items)
    st.write("Beverages:", beverages)
    if(Audio):
                st.write("Message recorded successfully")
                st.audio(Audio)
    st.write("Feedback:", feedback)
    