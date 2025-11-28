#Display the output
print("New Pyhon File")



url="https://api.spacexdata.com/v4/launches/past"
response = requests.get(url)
response.json()


data = pd.json_normalize(response.json())



# Web Scraping - parse Falcon 9 Launch Records - using beatifulsoup

# 1.wrangle data using API, 2.  3.deal with Null values - calc the mean, and replace nulls with mean
