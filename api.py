from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
import scraper, json

app = Flask(__name__)
api = Api(app)



class Home(Resource):
    def get(self):
        return send_from_directory('static', 'index.html')

class Destinations(Resource):
    def get(self):
        return scraper.getDestinations()

class Attractions(Resource):
    def get(self, country):
        city = request.args.get('city', default=None)
        sort = request.args.get('sort', default='ranked')
        return scraper.getAttractions(country, city, sort)

api.add_resource(Home, '/')
api.add_resource(Destinations, '/api/v0.1/atlas-obscura/destinations')
api.add_resource(Attractions, '/api/v0.1/atlas-obscura/attractions/<string:country>')

if __name__ == '__main__':
    app.run(debug=True)

















