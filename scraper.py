import urllib.parse
import requests
from bs4 import BeautifulSoup

def makeResponseData(status, name, data=None):
    response = {}
    response['status'] = status
    if data:
        response['results'] = len(data)
        response[name] = data
    else:
        response['results'] = None
        response[name] = None
    return response

def getDestinations(region): 
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

    # region parameter
    if region:
        return destinations[region.replace('-', ' ')]
    else:
        return destinations
        

def getAttractions(country, city, sort, limit, offset):
    # base url
    url = 'https://www.atlasobscura.com/things-to-do/'
    # specify CITY
    if city:
        url += city + '-'
    # specify COUNTRY
    url += country + '/places?'

    # QUERY PARAMS
    # specify PAGE
    if 0 < offset and offset <= 16:
        url += '&page=' + str(offset + 1)
    # specify SORT
    if sort == 'recent':
        url += '&sort=recent'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    attractions = []

    cards = soup.find_all('div', class_='index-card-wrap')
    limit = len(cards) if limit == 0 else limit
    for i in range(limit):
        card = cards[i]
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