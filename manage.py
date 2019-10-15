from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from os import environ


class WhatsApp(Resource):
    def get(self):
        return jsonify({"oi":"oioi"})

class NoRoute(Resource):
    def get(self):
        message = request.json
        return jsonify({'ola':'olaaa'})

app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)

api.add_resource(WhatsApp, '/wpp')
api.add_resource(NoRoute, '/')

app.run(debug=True, use_reloader=False, host='0.0.0.0', port=environ.get('PORT'))