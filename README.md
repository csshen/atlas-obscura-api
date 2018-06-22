# Atlas Obscura Unofficial API
![version 0.1.0](https://img.shields.io/badge/Release-v0.3.0-brightgreen.svg) ![python-flask](https://img.shields.io/badge/python-flask-orange.svg)  

A simple Flask-RESTful api for [Atlas Obscura](https://www.atlasobscura.com/).  
Hosted on Heroku [here](https://atlas-obscura-api.herokuapp.com/).

From the [wikipedia page](https://en.wikipedia.org/wiki/Atlas_Obscura):
> Atlas Obscura is an online magazine and digital media company led by American journalist David Plotz.

<!-- -->
> It catalogs unusual and obscure travel destinations, and relies heavily on user-generated content. It features a mixture of feature and news articles on topics including history, science and some news, in addition to travel and exploration, as well as hosting a collaborative "guide" to the world's most obscure places.

## API Documentation
![v0.3.0 | NEW!](https://img.shields.io/badge/Release%20v0.3.0-NEW!-brightgreen.svg)
### What's new in this version?
* Added endpoints for Gastro Obscura, a spinoff of Atlas Obscura for cuisine and restaurants.  
* Added query parameter to filter by U.S. state.

### Base URL
```
https://atlas-obscura-api.herokuapp.com
```
### Destinations
Use this endpoint to get a list of all destinations (countries) on Atlas Obscura.
```
/api/atlas/destinations
```
#### Parameters
| Name                 | Type   | Description              |
|:---------------------|:-------|:-------------------------|
| region `optional` | String | Specifies the geograpical region.<br>Default Value: `all`<br>Allowed values: `Africa`, `Antarctica`, `Asia`, `Caribbean`, `Central-America`, `Middle-East`, `North-America`, `Oceania`, `South-America`|

#### Sample Response
`GET` `https://atlas-obscura-api.herokuapp.com/api/atlas/destinations?region=Central-America`
```javascript
{
  status: "success",
  results: 6,
  region: "Central America",
  destinations: ["Belize", "Costa Rica", "Guatemala", "Honduras", "Nicaragua", "Panama"]
}

```


### Attractions
Use this endpoint to get a list of attractions in a particular country or city.
```
/api/atlas/attractions/<country>
```
#### Parameters
| Name                 | Type   | Description              |
|:---------------------|:-------|:-------------------------|
| country `required`   | String | Specifies country.<br>Allowed Values: `Abkhazia` `Afghanistan` `Albania` `Andorra` `Angola` `Antarctica` `Argentina` `Armenia` `Australia` `Austria` `Azerbaijan` `Bahamas` `Bahrain` `Bangladesh` `Barbados` `Belarus` `Belgium`  `Belize` `Benin` `Bermuda` `Bhutan` `Bolivia` `Bosnia-and-Herzegovina` `Botswana` `Brazil` `Brunei` `Bulgaria` `Cambodia` `Cameroon` `Canada` `Cape-Verde` `Cayman-Islands` `Chile` `China` `Colombia` `Costa-Rica` `Croatia` `Cuba` `Curacao` `Cyprus` `Czechia` `Democratic-Republic-of-the-Congo` `Denmark` `Dominica` `Dominican-Republic` `Ecuador` `Egypt` `Estonia` `Ethiopia` `Falkland-Islands` `Faroe-Islands` `Fiji` `Finland` `France` `French-Guiana` `French-Polynesia` `French-Southern-and-Antarctic-Lands` `Gabon` `Georgia` `Germany` `Ghana` `Greece` `Greenland` `Grenada` `Guadeloupe` `Guam` `Guatemala` `Haiti` `Honduras` `Hong-Kong` `Hungary` `Iceland` `India` `Indonesia` `Iran` `Iraq` `Ireland` `Israel` `Italy` `Ivory-Coast` `Jamaica` `Japan` `Jersey` `Jordan` `Kazakhstan` `Kenya` `Kyrgyzstan` `Laos` `Latvia` `Lebanon` `Liberia` `Libya` `Lithuania` `Luxembourg` `Macedonia` `Madagascar` `Malawi` `Malaysia` `Maldives` `Mali` `Malta` `Marshall-Islands` `Mauritania` `Mauritius` `Mexico` `Micronesia` `Moldova` `Monaco` `Mongolia` `Montenegro` `Montserrat` `Morocco` `Mozambique` `Namibia` `Nepal` `Netherlands` `New-Zealand` `Nicaragua` `Niger` `Nigeria` `North-Korea` `Northern-Mariana-Islands` `Norway` `Oman` `Pakistan` `Panama` `Peru` `Philippines` `Pitcairn-Islands` `Poland` `Portugal` `Puerto-Rico` `Qatar` `Republic-of-the-Congo` `Romania` `Russia` `Rwanda` `Saint-Vincent-and-the-Grenadines` `Samoa` `Sao-Tome-and-Principe` `Saudi-Arabia` `Senegal` `Serbia` `Seychelles` `Singapore` `Slovakia` `Slovenia` `South-Africa` `South-Korea` `Spain` `Sri-Lanka` `Sudan` `Sweden` `Switzerland` `Syria` `Taiwan` `Tajikistan` `Tanzania` `Thailand` `Timor-Leste` `Togo` `Tonga` `Trinidad-and-Tobago` `Tunisia` `Turkey` `Turkmenistan` `Turks-and-Caicos-Islands` `US-Virgin-Islands` `Uganda` `Ukraine` `United-Arab-Emirates` `United-Kingdom` `United-States` `Uruguay` `Uzbekistan` `Vanuatu` `Venezuela` `Vietnam` `Yemen` `Zambia` `Zimbabwe`|
| city `optional`      | String | Specifies city within country. If country is `United-States`, you must specify the state before you specify the city.<br>Default Value: `None`|
| state `optional`     | String | Specifies state within the United States (and D.C.)<br>Allowed Values: `Alabama` `Alaska` `Arizona` `Arkansas` `California`  `Colorado` `Connecticut` `Delaware` `Florida` `Georgia` `Hawaii` `Idaho` `Illinois` `Indiana` `Iowa` `Kansas` `Kentucky` `Louisiana` `Maine` `Maryland` `Massachusetts` `Michigan` `Minnesota` `Mississippi` `Missouri` `Montana` `Nebraska` `Nevada` `New-Hampshire` `New-Jersey` `New-Mexico` `New-York` `North-Carolina` `North-Dakota` `Ohio` `Oklahoma` `Oregon` `Pennsylvania` `Rhode-Island` `South-Carolina` `South-Dakota` `Tennessee` `Texas` `Utah` `Vermont` `Virginia` `Washington`  `West-Virginia` `Wisconsin` `Wyoming` `Washington-DC`<br>Default Value: `None`
| sort `optional`      | String | Sort by highest ranked or most recent.<br>Default Value: `ranked`<br>Allowed Values: `ranked` `recent`|
| limit `optional`     | Number | Specifies number of results to be returned.<br>Default Value: `auto`<br>Value Range `1 - 16`|
| offset `optional`    | Number | Results are paginated as on the website; each page returns a maximum of 16 results. Specifies offset from first page.<br>Default Value: `0`|

#### Sample Response
`GET` `https://atlas-obscura-api.herokuapp.com/api/atlas/attractions/japan?city=tokyo&sort=recent&limit=3`
```javascript
{
  status: "success",
  results: 3,
  attractions: [
    {
      name: "Intermediatheque",
      location: "Tokyo, Japan",
      description: "An unexpected curiosity cabinet hidden within a department store in the Japan Post tower.",
      coordinates: [35.6798, 139.7645],
      img: "https://assets.atlasobscura.com/media/...",
      path: "/places/intermediatheque"
    },
    {
      name: "Owl Police Box",
      location: "Tokyo, Japan",
      description: "This adorable birdlike police box is designed based on a play on words.",
      coordinates: [35.7297, 139.7129],
      img: "https://assets.atlasobscura.com/media/...",
      path: "/places/owl-police-box-ikebukuro-station"
    },
    {
      name: "Myth of Tomorrow",
      location: "Tokyo, Japan",
      description: "After being lost for decades, this striking mural depicting the atomic bomb covers the wall...",
      coordinates: [35.658, 139.7016],
      img: "https://assets.atlasobscura.com/media/...",
      path: "/places/myth-of-tomorrow"
    }
  ]
}
```
### Unique Food & Drink
Use these endpoints to get a list of cuisines of a particular country or city.
```
/api/gastro/food-and-drink
```
#### Parameters
| Name              | Type   | Description |
|-------------------|--------|-------------|
| region `optional` | String | Specifies the geograpical region.<br>Default Value: `all`<br>Allowed values: `Africa`, `Antarctica`, `Asia`, `Caribbean`, `Central-America`, `Middle-East`, `North-America`, `Oceania`, `South-America`|
| limit `optional`     | Number | Specifies number of results to be returned.<br>Default Value: `auto`<br>Value Range `1 - 16`|
| offset `optional`    | Number | Results are paginated as on the website; each page returns a maximum of 16 results. Specifies offset from first page.<br>Default Value: `0`|
```
/api/gastro/food-and-drink/<country>
```
#### Parameters
| Name              | Type   | Description |
|-------------------|--------|-------------|
| country `required`| String | Specifies country.<br>Default Value: `None`|
| limit `optional`     | Number | Specifies number of results to be returned.<br>Default Value: `auto`<br>Value Range `1 - 16`|
| offset `optional`    | Number | Results are paginated as on the website; each page returns a maximum of 16 results. Specifies offset from first page.<br>Default Value: `0`|

#### Sample Response
`GET` `https://atlas-obscura-api.herokuapp.com/api/gastro/food-and-drink/south-korea?limit=2`
```javascript
{
  status: "success",
  results: 2,
  unique-food-and-drink: [
    {
      category: "Sweets",
      name: "Dragon's Beard Candy",
      region: "South-Korea",
      description: "The ancient confection consists of wispy sugar-strands that look like dragon whiskers.",
      img: "https://assets.atlasobscura.com/media/...",
      path: "/foods/dragons-beard-candy-china"
    },
    {
      category: "Drinks",
      name: "Makgeolli",
      region: "South-Korea",
      description: "South Korea's oldest alcoholic beverage is making a comeback.",
      img: "https://assets.atlasobscura.com/media/...",
      path: "/foods/makgeolli-south-korea"
    }
  ]
}
```
### Gastro Places
Use this endpoint to return Gastro Obscura places and restaurants.
```
/api/gastro/places
```
#### Parameters
| Name              | Type   | Description |
|-------------------|--------|-------------|
| limit `optional`     | Number | Specifies number of results to be returned.<br>Default Value: `auto`<br>Value Range `1 - 18`|
| offset `optional`    | Number | Results are paginated as on the website; each page returns a maximum of 18 results. Specifies offset from first page.<br>Default Value: `0`|

#### Sample Response
`GET` `https://atlas-obscura-api.herokuapp.com/api/gastro/places?limit=2`
```javascript
{
  status: "success",
  results: 2,
  Gastro-Places: [
    {
      location: "Savannah, Georgia",
      name: "The Pirates' House",
      description: "This kitschy tavern is also home to rare early editions of \"Treasure Island.\"",
      coordinates: [32.0781, -81.0839],
      img: "https://assets.atlasobscura.com/media/...",
      path: "/places/the-pirates-house"},
    {
      location: "Lisbon, Portugal",
      name: "Conserveira de Lisboa",
      description: "The best place in the world to buy canned fish. ",
      coordinates: [38.7093, -9.1347],
      img: "https://assets.atlasobscura.com/media/...",
      path: "/places/conserveira-de-lisboa"
    }
  ]
}
```
