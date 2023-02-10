import os
import csv
import requests
from bs4 import BeautifulSoup

def data_scraping():
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
		world_data.append(countries)
	   
	del world_data[0]
	# #print (world_data)

	#Write the scraped data to a csv file. 
	try: 
		os.mkdir("./data")
	except OSError as error:
		print("It already created")
	str_names = ["Country", "Total Cases", "New Cases", "Total Deaths", "New Deaths",
	 			"Total Recovered", "New Recovered", "Active Cases", "Serious Critical",
	 			"Tot cases/1M pop","Deaths/1M pop","Total Tests", "Tests/1M pop","Population"]
	newFile = "./data/covid19-stats.csv"
	print (newFile)

	with open(newFile, "w", newline = "") as f:
		writer = csv.writer(f)
		writer.writerow(str_names)
		for cy in world_data:
			writer.writerow(cy)

	# A quick data cleaning that removes unnecessary contents and convert the data
	# type into integers.
	with open("./data/covid19-stats.csv", "r") as f:
		reader = csv.reader(f)
		data = list(reader)

	# Get the header row
	rows = data[0]

	# Get the rest of the rows
	rest = data[1:]

	# Remove any rows that don't have data
	rest = [r for r in rest if r]

	# Loop through each row and clean the data
	cleaned_rows = []
	for r in rest:
		cleaned_row = []
		for cell in r:
			# Remove commas from the numbers
			cell = cell.replace(",", "")
			# Try to convert the cell to a number
			try:
				cell = int(cell)
			except ValueError:
				pass
			cleaned_row.append(cell)
		cleaned_rows.append(cleaned_row)

data_scraping()