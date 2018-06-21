# Atlas Obscura Unofficial API
![version 0.1.0](https://img.shields.io/badge/Version-0.1.0-brightgreen.svg) ![python-flask](https://img.shields.io/badge/python-flask-orange.svg)  
  
A simple Flask-RESTful api for [Atlas Obscura](https://www.atlasobscura.com/).  
Hosted on Heroku [here](https://atlas-obscura-api.herokuapp.com/).

From the [wikipedia page](https://en.wikipedia.org/wiki/Atlas_Obscura):
> Atlas Obscura is an online magazine and digital media company led by American journalist David Plotz.

<!-- -->
> It catalogs unusual and obscure travel destinations, and relies heavily on user-generated content. It features a mixture of feature and news articles on topics including history, science and some news, in addition to travel and exploration, as well as hosting a collaborative "guide" to the world's most obscure places.

## API Documentation
Version 0.1.0  
### Base URL
```
https://atlas-obscura-api.herokuapp.com
```
### Destinations Endpoint
```
/api/destinations
```
#### Parameters
| Name                 | Type   | Description              |
|:---------------------|:-------|:-------------------------|
| region `optional` | String | Specifies the geograpical region.<br>Default Value: `all`<br>Allowed values: `Africa`, `Antarctica`, `Asia`, `Caribbean`, `Central-America`, `Middle-East`, `North-America`, `Oceania`, `South-America`|

#### Sample Response
`GET` `https://atlas-obscura-api.herokuapp.com/api/destinations?region=Central-America`
```javascript
{
  status: "success",
  results: 6,
  region: "Central America",
  destinations: ["Belize", "Costa Rica", "Guatemala", "Honduras", "Nicaragua", "Panama"]
}

```


### Attractions Endpoint
```
https://atlas-obscura-api.herokuapp.com/api/attractions/<country>
```
#### Parameters
| Name                 | Type   | Description              |
|:---------------------|:-------|:-------------------------|
| country `required`   | String | Specifies country.<br>Allowed Values: `Abkhazia`, `Afghanistan`, `Albania`, `Andorra`, `Angola`, `Antarctica`, `Argentina`, `Armenia`, `Australia`, `Austria`, `Azerbaijan`, `Bahamas`, `Bahrain`, `Bangladesh`, `Barbados`, `Belarus`, `Belgium`, `Belize`, `Benin`, `Bermuda`, `Bhutan`, `Bolivia`, `Bosnia-and-Herzegovina`, `Botswana`, `Brazil`, `Brunei`, `Bulgaria`, `Cambodia`, `Cameroon`, `Canada`, `Cape-Verde`, `Cayman-Islands`, `Chile`, `China`, `Colombia`, `Costa-Rica`, `Croatia`, `Cuba`, `Curacao`, `Cyprus`, `Czechia`, `Democratic-Republic-of-the-Congo`, `Denmark`, `Dominica`, `Dominican-Republic`, `Ecuador`, `Egypt`, `Estonia`, `Ethiopia`, `Falkland-Islands`, `Faroe-Islands`, `Fiji`, `Finland`, `France`, `French-Guiana`, `French-Polynesia`, `French-Southern-and-Antarctic-Lands`, `Gabon`, `Georgia`, `Germany`, `Ghana`, `Greece`, `Greenland`, `Grenada`, `Guadeloupe`, `Guam`, `Guatemala`, `Haiti`, `Honduras`, `Hong-Kong`, `Hungary`, `Iceland`, `India`, `Indonesia`, `Iran`, `Iraq`, `Ireland`, `Israel`, `Italy`, `Ivory-Coast`, `Jamaica`, `Japan`, `Jersey`, `Jordan`, `Kazakhstan`, `Kenya`, `Kyrgyzstan`, `Laos`, `Latvia`, `Lebanon`, `Liberia`, `Libya`, `Lithuania`, `Luxembourg`, `Macedonia`, `Madagascar`, `Malawi`, `Malaysia`, `Maldives`, `Mali`, `Malta`, `Marshall-Islands`, `Mauritania`, `Mauritius`, `Mexico`, `Micronesia`, `Moldova`, `Monaco`, `Mongolia`, `Montenegro`, `Montserrat`, `Morocco`, `Mozambique`, `Namibia`, `Nepal`, `Netherlands`, `New-Zealand`, `Nicaragua`, `Niger`, `Nigeria`, `North-Korea`, `Northern-Mariana-Islands`, `Norway`, `Oman`, `Pakistan`, `Panama`, `Peru`, `Philippines`, `Pitcairn-Islands`, `Poland`, `Portugal`, `Puerto-Rico`, `Qatar`, `Republic-of-the-Congo`, `Romania`, `Russia`, `Rwanda`, `Saint-Vincent-and-the-Grenadines`, `Samoa`, `Sao-Tome-and-Principe`, `Saudi-Arabia`, `Senegal`, `Serbia`, `Seychelles`, `Singapore`, `Slovakia`, `Slovenia`, `South-Africa`, `South-Korea`, `Spain`, `Sri-Lanka`, `Sudan`, `Sweden`, `Switzerland`, `Syria`, `Taiwan`, `Tajikistan`, `Tanzania`, `Thailand`, `Timor-Leste`, `Togo`, `Tonga`, `Trinidad-and-Tobago`, `Tunisia`, `Turkey`, `Turkmenistan`, `Turks-and-Caicos-Islands`, `US-Virgin-Islands`, `Uganda`, `Ukraine`, `United-Arab-Emirates`, `United-Kingdom`, `United-States`, `Uruguay`, `Uzbekistan`, `Vanuatu`, `Venezuela`, `Vietnam`, `Yemen`, `Zambia`, `Zimbabwe`|
| city `optional`      | String | Specifies city within country.<br>Default Value: `None`|
| sort `optional`      | String | Sort by highest ranked or most recent.<br>Default Value: `ranked`<br>Allowed Values: `ranked`, `recent`|
| limit `optional`     | Number | Specifies number of results to be returned.<br>Default Value: `auto`<br>Value Range `1 - 16`|
| offset `optional`    | Number | Results are paginated; specifies offset from first page<br>Default Value: `0`|

#### Sample Response
`GET` `https://atlas-obscura-api.herokuapp.com/api/attractions/japan?city=tokyo&sort=recent&limit=4`
```javascript
{
  status: "success",
  results: 4,
  attractions: [
    {
      name: "Intermediatheque",
      city: "Tokyo",
      country: "Japan",
      description: "An unexpected curiosity cabinet hidden within a department store in the Japan Post tower.",
      coordinates: [35.6798, 139.7645]
    },
    {
      name: "Owl Police Box",
      city: "Tokyo",
      country: "Japan",
      description: "This adorable birdlike police box is designed based on a play on words.",
      coordinates: [35.7297, 139.7129]
    },
    {
      name: "Myth of Tomorrow",
      city: "Tokyo",
      country: "Japan",
      description: "After being lost for decades, this striking mural depicting the atomic bomb covers the wall of a busy Tokyo metro station.",
      "coordinates": [35.658, 139.7016]
    },
    {
      name: "Detective Bar Progress",
      city: "Tokyo",
      country: "Japan",
      description: "The bartenders at this crime-fighting theme cafe are actual private detectives by day.",
      coordinates: [35.7334, 139.7112]
    }
  ]
}
```
