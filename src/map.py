import os
import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

# start this porject with data scraping from the web, then start design the layout 
# of a dashboard with css or other language. - 1/1/202

def scraped_data():
	# An actual website link that will be used to scrape and analyze.
	# A quick note: the website link below is open-source and free. 
	url = "https://www.worldometers.info/coronavirus/"

	# Send a request to the website.
	permission = requests.get(url)

	# A quick check for the requested data.
	code = requests.status_codes
	if not code:
		print ("Error.")
	
	# start parsing
	fileContent = BeautifulSoup(permission.text, "html.parser") # It actually prints entire html info. 
	dataTable = fileContent.find("table", id = "main_table_countries_today").find("tbody")
	rows = dataTable.find_all("tr", style = "")

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
	#print (world_data[0:10])

	#Write the scraped data to a csv file. (Try to fix this tomorrow)
	# try: 
	# 	os.mkdir("./tmp")
	# except OSError as error:
	# 	print("It already created")
	# str_names = ["Country", "Total Cases", "New Cases", "Total Deaths",
	# 			"Total Recovered", "Active Cases", "Total Tests", "Population"]
	# newFile = "./tmp/covid19-stats.csv"
	# print (newFile)

	# with open(newFile, "w", newline = "") as f:
	# 	writer = csv.writer(f)
	# 	writer.writerow(str_names)
	# 	for cy in world_data:
	# 		writer.writerow(cy)

	data = pd.read_csv('covid19-stats.csv')
	print (data.head(10))


def board():

# Call the functions.
scraped_data()
board()