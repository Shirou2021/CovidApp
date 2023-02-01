import os
import pandas as pd
from PIL import Image
import streamlit as st
import plotly.express as px

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


options = st.sidebar.selectbox("Options", ('Bar Chart', 'Pie Chart', 'Line Graph', 'HeatMap'))
regions = st.sidebar.selectbox("Select a region", df['Countries'].unique())
status = st.sidebar.selectbox("Current Status", ('Total Cases', 'Total Deaths', 'Total Recovered', 'Active Cases'))
visuals = df[df['Countries'] == regions]
st.markdown(""" # Global View """)


def data_frame(df):
	final_df = pd.DataFrame({
    'Status':['Total Cases', 'Total Deaths', 'Recovered','Active'],
    'Number of cases':(df.iloc[0]['Total Cases'],
    df.iloc[0]['Total Deaths'], 
    df.iloc[0]['Total Recovered'], df.iloc[0]['Active Cases'])})
	return final_df

gTotal = data_frame(visuals)
def chart():
	#................................................................
	if options == 'Bar Chart':
		final_graph = px.bar(gTotal, x = 'Status', y = 'Number of cases',  labels={'Number of cases':'Number of cases in %s' % (regions)},color='Status')
		st.plotly_chart(final_graph)
	
	if options == 'Pie Chart':
		if status == "Total Cases":
			output = px.pie(df, values= df["Total Cases"], names = df["Countries"])
			st.plotly_chart(output)
		elif status == "Total Deaths":
			output = px.pie(df, values = df["Total Deaths"], names = df["Countries"])
			st.plotly_chart(output)
		elif status == "Total Recovered":
			output = px.pie(df, values = df["Total Recovered"], names = df["Countries"])
			st.plotly_chart(output)
		elif status == "Active Cases":
			output = px.pie(df, values = df["Actice Cases"], names = df["Countries"])
			st.plotly_chart(output)

	if options == "Line Graph":
		if status == "Total Cases":
			output2 = px.line (df, x = 'Countries', y = df["Total Cases"])
			st.plotly_chart(output2)
		elif status == "Active Cases":
			output2 = px.line (df, x = 'Countries', y = df["Active Cases"])
			st.plotly_chart(output2)
		elif status == "Total Deaths":
			output2 = px.line (df, x = 'Countries', y = df["Total Deaths"])
			st.plotly_chart(output2)
		elif status == "Total Recovered":
			output2 = px.line (df, x = 'Countries', y = df["Total Recovered"])
			st.plotly_chart(output2)

		# if options == "HeatMap":
			
chart()
