#Display the output
print("New Pyhon File")



url="https://api.spacexdata.com/v4/launches/past"
response = requests.get(url)
response.json()
