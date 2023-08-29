import streamlit as st
import pandas as pd

data = {
    "Fruit": ["Sam Curran","Tom Curran","Sam Billings","Tom Hardy","Virat Kohli","I Pathan","Y Pathan"],
    "Color": ["Red", "Yellow", "Red", "Brown", "Purple", "Purple", "Brown"]
}

df = pd.DataFrame(data)

selection = st.selectbox("Select an option:", df["Fruit"], key="dropdown")

if selection:
    filtered_df = df[df["Fruit"] == selection]

    st.write("Filtered Data:")
    st.write(filtered_df)
