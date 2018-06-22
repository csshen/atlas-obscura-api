from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
import scraper, json

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html', test="TEST"),200,headers)

class Destinations(Resource):
    def get(self):
        try:
            region = request.args.get('region', default=None)
            data = scraper.getDestinations(region)
            if region:
                data['region'] = region
            return scraper.makeResponseData('success', 'Destinations', data)
        except:
            return scraper.makeResponseData('failure', 'Destinations')

class Attractions(Resource):
    def get(self, country):
        try:
            city = request.args.get('city', default=None)
            state = request.args.get('state', default=None)
            sort = request.args.get('sort', default='ranked')
            limit = request.args.get('limit', type=int, default=16)
            offset = request.args.get('offset', type=int, default=0)
            data = scraper.getAttractions(country, city, state,
            sort, limit, offset)
            return scraper.makeResponseData('success', 'Attractions', data)
        except:
            return scraper.makeResponseData('failure', 'Attractions')

class FoodandDrink1(Resource):
    def get(self):
        try:
            offset = request.args.get('offset', type=int, default=0)
            limit = request.args.get('limit', type=int, default=16)
            region = request.args.get('offset', default=None)
            data = scraper.getFoodandDrink(None, offset, limit, region)
            return scraper.makeResponseData('success',
            'unique-food-and-drink', data)
        except:
            return scraper.makeResponseData('failure',
            'unique-food-and-drink')

class FoodandDrink2(Resource):
    def get(self, country):
        try:
            offset = request.args.get('offset', type=int, default=0)
            limit = request.args.get('limit', type=int, default=16)
            data = scraper.getFoodandDrink(country, offset, limit)
            return scraper.makeResponseData('success',
            'unique-food-and-drink', data)
        except:
            return scraper.makeResponseData('failure', 'unique-food-and-drink')

class GastroPlaces(Resource):
    def get(self):
        try:
            offset = request.args.get('offset', type=int, default=0)
            limit = request.args.get('limit', type=int, default=18)
            data = scraper.getGastroPlaces(offset, limit)
            return scraper.makeResponseData('success', 'Gastro-Places', data)
        except:
            return scraper.makeResponseData('failure', 'Gastro-Places')

api.add_resource(Home, '/')
api.add_resource(Destinations, '/api/atlas/destinations')
api.add_resource(Attractions,  '/api/atlas/attractions/<string:country>')
api.add_resource(FoodandDrink1, '/api/gastro/food-and-drink')
api.add_resource(FoodandDrink2, '/api/gastro/food-and-drink/<string:country>')
api.add_resource(GastroPlaces,  '/api/gastro/places')

if __name__ == '__main__':
    app.run()
