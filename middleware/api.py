
# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import os
import src.db as db
import src.readme as readme
app = Flask(__name__)
# Create the API
api = Api(app)

@app.route('/')
def index():
    return readme.render(os.path.dirname(app.root_path) + '/app/Readme.md')


# see
# https://github.com/jakewright/tutorials/blob/master/home-automation/02-device-registry/device_registry/__init__.py
class Collection(Resource):
    def get(self, identifier):
        coldb = db.CollectionsDb()

        return {'message': 'Success', 'data': coldb.get(identifier)}, 200



api.add_resource(Collection, '/api/v1/collection/<string:identifier>')