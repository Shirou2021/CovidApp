import os
import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
import streamlit as strl
# start this porject with data scraping from the web, then start design the layout 
# of a dashboard with css or other language. - 1/1/202

def scraped_data():
	# An actual website link that will be used to scrape and analyze.
	# A quick note: the website link below is open-source and free. 
	url = "https://www.worldometers.info/coronavirus"

	# Send a request to the website.
	permission = requests.get(url)


	# A quick check for the requested data.
	code = requests.status_codes
	if not code:
		print ("Error.")
	
	# start parsing
	fileContent = BeautifulSoup(permission.content, features ='html.parser') # It actually prints entire html info. 
	fileContent.prettify()
	dataTable = fileContent.find('table', attrs={'id': 'main_table_countries_today'}).find("tbody")
	#dataTable = fileContent.find("table", id = "main_table_countries_today").find("tbody")
	rows = dataTable.find_all("tr", attrs={"style": ""})

	# A quick for loop that iterate through each row 
	world_data = []
	for info in rows:
		cols = info.find_all("td")
		countries = [c.text.strip() for c in cols]
		del countries[0]
		del countries[5]
		del countries[7]
		del countries[9]
		del countries[10]
		del countries[11]
		del countries[13]
		world_data.append(countries)
			
	   
	del world_data[0]
	# #print (world_data)

	#Write the scraped data to a csv file. 
	try: 
		os.mkdir("./tt")
	except OSError as error:
		print("It already created")
	str_names = ["Country", "Total Cases", "New Cases", "Total Deaths",
	 			"Total Recovered", "Active Cases", "Total Tests", "Population"]
	newFile = "./tt/covid19-stats.csv"
	print (newFile)

	with open(newFile, "w", newline = "") as f:
		writer = csv.writer(f)
		writer.writerow(str_names)
		for cy in world_data:
			writer.writerow(cy)
	# dt = pd.DataFrame(world_data[1:], columns=world_data[0][:12])
	# #df.to_csv('coronavirus.csv')
	
	# # dt = pd.DataFrame(world_data[1:], columns=world_data[0][:12]) #Formatting the header
	# df = dd.from_pandas(dt,npartitions=1)
	# print(df.head())

	#data = pd.read_csv('./tt/covid19-stats.csv')
	# print (data.head(10))
	#print (data ["Country"] == "Spain") 

	#live_data.iloc[:, :].to_csv("covid.csv")


def read(): # if the data frame can;t read the data properly, then manually change the csv file since the website updates frequently.
	data = pd.read_csv('./tt/covid19-stats.csv')
	return data

data = read()
def base_format():
	# data = pd.read_csv('./tt/covid19-stats.csv')
	# # #print (data.head(10))
	# print (data['Country'] == 'Spain')
	strl.title('World Wide Covid19 stats!')
	strl.sidebar.title("Pick a choice")
	visuals = strl.sidebar.selectbox('Choose a pick viusal representation', (types of chart.....))
	country = strl.sidebar.selectbox('Choose a country to visualize' data...)
	records = strl.sidebar.radio('Virus status', (different status.))
	selected_territory = data[data['country'] == country]
	strl.markdown('Country-level Analysis')

	return True 
def data_parsing(data):
	newFrame = pd.DataFrame({'status'}: [Status variables and use df.loc or df.iloc.])
	return newFrame
country_total = data_parsing(selected_territory)

if visual == 'Bar Chart':
	graph = px.bar(country_total, x = 'Status', y = 'number of cases', label = {'number of cases': (country)}, color = 'status')
	strl.plotly_chart(graph)

if visual == 'Pie Chart':
	if records == "confirmed cases":
		strl.title('xxx')
		fig = px.pie(data, values = data['confirmed cases'], names = data['country'])
		strl.plotly_chart(fig)
	elif records == "....":
		strl.title('xxx')
		fig = px.pie(data, values = data['...'], names = data['country'])
		strl.plotly_chart(fig)
	elif records == "....":
		strl.title('xxx')
		fig = px.pie(data, values = data['...'], names = data['country'])
		strl.plotly_chart(fig)
	elif records == "....":
		strl.title('xxx')
		fig = px.pie(data, values = data['...'], names = data['country'])
		strl.plotly_chart(fig)
	else:
		strl.title('xxx')
		fig = px.pie(data, values = data['...'], names = data['country'])
		strl.plotly_chart(fig)

if visual = "Line Chart":
	if records == "confirmed cases":
		strl.title('xxx')
		fig = px.pie(data, values = data['confirmed cases'], names = data['country'])
		strl.plotly_chart(fig)
	# Same as above.
def _main_():
	scraped_data()
	read()
	board()

_main_() # Calls the final function to perform all the functionality within this program. 
