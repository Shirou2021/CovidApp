import os
import pandas as pd
from PIL import Image
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def design():
	st.write("""# Covid19 Dashboard 
		This dashboard aims to provide a quick overview of covid19 status. """)
	st.sidebar.title("Home Menu")
	photo = Image.open("Vex.jpg")
	photo.show()
	st.image(photo, use_column_width = True)

	# Fix the markdown css part. Finish this when the project is almost done for visual effect.
	st.markdown('<style>body{background-color: darkblue;}</style', unsafe_allow_html = True)
design()

@st.cache
def read_file():
	data = pd.read_csv("covid19_info.csv")
	return data

df = read_file()

def sidebar():
	options = st.sidebar.selectbox("Options", ('Bar Chart', 'Pie Chart', 'Line Chart', 'HeatMap'))
	regions = st.sidebar.selectbox("Select a region", df['Countries'].unique())
	status = st.sidebar.selectbox("Current Status", ('Total cases', 'Death Cases', 'Recovered Cases', 'Active Cases'))
	visuals = df[df['Countries'] == regions]
	st.markdown(""" # Global View """)

sidebar()

def data_frame(self):
	final_df = pd.DataFrame({''})

def chart():
	#................................................................
	if something:
		#bb

if __name__ == '__chart__':
	chart()
