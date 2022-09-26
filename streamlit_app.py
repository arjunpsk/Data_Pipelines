
import gspread

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import streamlit as st

def read_data():
    gc = gspread.service_account(filename="service_account.json")
    sh = gc.open("CAB Data Pipeline").get_worksheet(0) # index 0 = sheet1, index 1 = sheet2, etc.
    df = pd.DataFrame(sh.get_all_records())
    return df

def plot_data():
    df = read_data()
    df['price'] = df['price'].astype(float)

    fig = px.line(data_frame = df, 
                x = 'date' ,
                y = 'price')
    st.plotly_chart(fig)
    
plot_data()

