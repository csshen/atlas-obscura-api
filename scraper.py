import urllib.parse
import requests
from bs4 import BeautifulSoup

def getDestinations(): 
    url = 'https://www.atlasobscura.com/destinations'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    destinations = {}
    for item in soup.find_all('li', class_='global-region-item'):
        continent_soup = item.div
        continent_name = continent_soup.h2.text.strip()
        destinations[continent_name] = []
        for country in continent_soup.find_all('a', class_='detail-md non-decorated-link'):
            destinations[continent_name].append(country.text);

    return destinations
        

def getAttractions(country, city, sort):
    # base url
    url = 'https://www.atlasobscura.com/things-to-do/'
    # specify CITY
    if city:
        url += city + '-'
    # specify COUNTRY
    url += country + '/places'
    # specify SORT
    if sort == 'recent':
        url += '?sort=recent'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    attractions = []
    for card in soup.find_all('div', class_='index-card-wrap'):
        # CREATE NEW ATTRACTION
        curr_attraction = {}

        # LOCATION (City, Town)
        location = card.find('div', class_='detail-sm place-card-location').text.split(',')
        # NAME
        name = card.find('span', class_='title-underline js-title-content').text
        # Description
        d = card.find('div', class_='subtitle-sm content-card-subtitle js-subtitle-content').text
        # Coordinates
        coord = [float(c) for c in card.find('div', class_='lat-lng').text.split(',')]

        curr_attraction['name'] = name
        curr_attraction['city'] = location[0]
        curr_attraction['country'] = location[1].strip()
        curr_attraction['description'] = d
        curr_attraction['coordinates'] = coord

        attractions.append(curr_attraction)


    return attractions


#response = getAttractions('germany', 'berlin')
#print(json.dumps(response, separators=(',',':'), indent=3))