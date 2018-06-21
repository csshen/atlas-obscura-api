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
            sort = request.args.get('sort', default='ranked')
            limit = request.args.get('limit', type=int, default=0)
            offset = request.args.get('offset', type=int, default=0)
            data = scraper.getAttractions(country, city, sort, limit, offset)
            return scraper.makeResponseData('success', 'Attractions', data)
        except:
            return scraper.makeResponseData('failure', 'Attractions')

api.add_resource(Home, '/')
api.add_resource(Destinations, '/api/destinations')
api.add_resource(Attractions,  '/api/attractions/<string:country>')

if __name__ == '__main__':
    app.run()

















