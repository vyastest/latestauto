import streamlit as st
import pandas as pd

data = {
    "Fruit": ["Sam Curran","Tom Curran","Sam Billings","Tom Hardy","Virat Kohli","I Pathan","Y Pathan"],
    "Color": ["Red", "Yellow", "Red", "Brown", "Purple", "Purple", "Brown"]
}

df=pd.read_csv("teststream.csv")
unique_players = df["striker"].unique()

selection = st.selectbox("Select an option:", unique_players, key="dropdown")

if selection:
    filtered_df = df[df["striker"] == selection]

    st.write("Filtered Data:")
    st.write(filtered_df)
