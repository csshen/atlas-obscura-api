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


def getAttractions(country, city, state, sort, limit, offset):
    # base url
    url = 'https://www.atlasobscura.com/things-to-do/'
    # specify CITY
    #if country == 'United-States' and state:
    #    country = state
    if city:
        url += city + '-'
    if state:
        country = state
    # specify COUNTRY
    url += country + '/places?'
    # QUERY PARAMS
    # specify PAGE
    if 0 < offset:
        url += '&page=' + str(offset + 1)
    # specify SORT
    if sort == 'recent':
        url += '&sort=recent'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    attractions = []

    for card in soup.find_all('a',
    class_='content-card content-card-place')[:limit]:
        # CREATE NEW ATTRACTION
        curr_attraction = {}
        # LOCATION (City, Town)
        curr_attraction['location'] = card.find('div',
        class_='detail-sm place-card-location').text
        # NAME
        curr_attraction['name'] = card.find('span',
        class_='title-underline js-title-content').text
        # Description
        curr_attraction['description'] = card.find('div',
        class_='subtitle-sm content-card-subtitle js-subtitle-content').text
        # Coordinates
        curr_attraction['coordinates'] = [float(c) for c in card.find('div',
        class_='lat-lng').text.split(',')]
        # Image Thumbnail
        curr_attraction['img'] = card.find('img')['data-src']
        # PATH
        curr_attraction['path'] = card['href']

        attractions.append(curr_attraction)

    return attractions

def getFoodandDrink(country, offset, limit, region=None):
    foods = []
    url = 'https://www.atlasobscura.com/unique-food-drink'
    if country:
        url += ('/' + country)
        if offset != 0:
            url += '?page=' + str(offset + 1)
    if region:
        url += '#' + region.replace('-', '%20')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    cards = soup.find_all('a', class_='content-card food-card')
    if country:
        start = 0
        end = limit
    else:
        start = offset * 16
        end = start + limit
    for card in cards[start:end]:
        curr_food = {}
        # CATEGORY
        curr_food['category'] = card.find('div',
        class_='detail-sm food-card-label food-card-supertag').text
        # NAME
        curr_food['name'] = card.find('h3',
        class_='title-md content-card-title').text.strip()
        # REGION
        if region:
            curr_food['region'] = card.parent['data-region'][2:-2]
        elif country:
            curr_food['region'] = country
        # DESCRIPTION
        curr_food['description'] = card.find('div',
        class_='content-card-subtitle content-card-subtitle-food'
        ' js-subtitle-content').text
        # IMAGE THUMBNAIL
        curr_food['img'] = card.find('img')['data-src']
        # PATH
        curr_food['path'] = card['href']
        # ADD Food
        foods.append(curr_food)

    return foods

def getGastroPlaces(offset, limit):
    # base url
    url = 'https://www.atlasobscura.com/gastro/places?'
    # QUERY PARAMS
    # specify PAGE
    if 0 < offset and offset <= 18:
        url += '&page=' + str(offset + 1)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    places = []

    for card in soup.find_all('a',
    class_='content-card content-card-place')[:limit]:
        # CREATE NEW ATTRACTION
        curr_place = {}

        # LOCATION (City, Town)
        curr_place['location'] = card.find('div',
        class_='detail-sm place-card-location').text
        # NAME
        curr_place['name'] = card.find('span',
        class_='title-underline js-title-content').text
        # Description
        curr_place['description'] = card.find('div',
        class_='subtitle-sm content-card-subtitle js-subtitle-content').text
        # Coordinates
        curr_place['coordinates'] = [float(c) for c in card.find('div',
        class_='lat-lng').text.split(',')]
        # Image Thumbnail
        curr_place['img'] = card.find('img')['data-src']
        # PATH
        curr_place['path'] = card['href']

        places.append(curr_place)

    return places

# TEST CODE HERE
#response = getAttractions('germany', 'berlin')
#print(json.dumps(response, separators=(',',':'), indent=3))
