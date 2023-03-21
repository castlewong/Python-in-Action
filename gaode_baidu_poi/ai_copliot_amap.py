import requests
import csv

# set up Amap Web API key and search parameters
api_key = 'd89a69807995de229a156eaad31b796b'
search_url = 'https://restapi.amap.com/v3/place/text'
keywords = '大学'  # search keyword
city = '六安'  # search city
output = 'json'

# send request to Amap Web API to get POI data
params = {
    'keywords': keywords,
    'city': city,
    'output': output,
    'key': api_key
}
response = requests.get(search_url, params=params)

# process response to get POI data
if response.status_code == 200:
    pois = response.json()['pois']
    # open CSV file for writing
    with open('pois.csv', mode='w', encoding='utf-8', newline='') as csv_file:
        # create CSV writer
        writer = csv.writer(csv_file)
        # write header row
        writer.writerow(['Name', 'Location'])
        # write data rows
        for poi in pois:
            writer.writerow([poi['name'], poi['location']])
    print(f"Saved {len(pois)} POIs to pois.csv")
else:
    print(response.text)

