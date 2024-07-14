import numpy as np
import streamlit as st
import pandas as pd

st.title('Clean My Data')
file = st.file_uploader('Please upload a csv file')

st.sidebar.title('What do you want to do?')
options = ['Remove Duplicates','Remove Rows with NaN Values']
opt = st.sidebar.selectbox('From my Data ',options)
df = pd.DataFrame()
temp_df = pd.DataFrame()
if file != None:
    df = pd.read_csv(file)
if opt == 'Remove Duplicates' :
    temp_df = df.drop_duplicates()
elif opt == 'Remove Rows with NaN Values':
    temp_df = df.dropna(axis=0)

st.download_button(label='Download CSV File', data=temp_df.to_csv().encode('utf-8'), file_name='CleanedFile.csv')
