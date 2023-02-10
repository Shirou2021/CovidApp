import os
import pandas as pd
from PIL import Image
import streamlit as st
import plotly.express as px

st.set_page_config(page_title = "Covid19 Visualizations")
def design():
	st.write("""# Covid19 Dashboard 
		This dashboard aims to provide a quick overview of covid19 status. """)
	st.sidebar.title("Home Menu")
	photo = Image.open("covid19.jpeg") # source: https://www.complianceweek.com/risk-management/coronavirus-tips-for-risk-management/28533.article
	photo.show()
	st.image(photo, use_column_width = True)

	st.markdown('<style>body{background-color: #080808}</style>', unsafe_allow_html = True)

design()

# Adds background image. The result might varies based on the version of streamlit package. 
def set_background_img():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images7.alphacoders.com/900/900403.jpg");
             background-size: cover;
			 background-position: center;
			 font: "serif"

         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_background_img()

@st.cache
def read_file():
	data = pd.read_csv("covid19_info.csv")
	return data

df = read_file()


options = st.sidebar.selectbox("Options", ('None', 'Bar Chart', 'Pie Chart', 'Line Graph', 'Scatter plot'))
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
def main():
	#................................................................

	# If user chooses "none" for options of chart or region is not selected, then no graph(s) will pop out. 
	if options == "None":
		return
	elif regions == "None":
		return

	# Bar chart of a particular country if selected
	if options == 'Bar Chart':
		final_graph = px.bar(gTotal, x = 'Status', y = 'Number of cases',  labels={'Number of cases':'Number of cases in %s' % (regions)},color='Status')
		st.plotly_chart(final_graph)

	# Pie chart for country-level visualization
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
	# Same as pie chart. 
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

	# global visualization based on status.
	if options == "Scatter plot":
		#output3 = px.scatter (df, x = "Countries", y = "Status", color = "Status2")
		if status == "Total Cases":
			output3 = px.scatter (df, x = df['Countries'], y = df["Total Cases"])
			st.plotly_chart(output3)
		elif status == "Active Cases":
			output3 = px.scatter (df, x = df['Countries'], y = df["Active Cases"])
			st.plotly_chart(output3)
		elif status == "Total Deaths":
			output3 = px.scatter (df, x = df['Countries'], y = df["Total Deaths"])
			st.plotly_chart(output3)
		elif status == "Total Recovered":
			output3 = px.scatter (df, x = df['Countries'], y = df["Total Recovered"])
			st.plotly_chart(output3)

if __name__ == "__main__":
	main()