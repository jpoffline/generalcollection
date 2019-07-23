import markdown
# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import os
import src.db as db

app = Flask(__name__)
# Create the API
api = Api(app)

@app.route('/')
def index():
    with open(os.path.dirname(app.root_path) + '/app/Readme.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


# see
# https://github.com/jakewright/tutorials/blob/master/home-automation/02-device-registry/device_registry/__init__.py
class Collection(Resource):
    def get(self, identifier):
        coldb = db.CollectionsDb()

        return {'message': 'Success', 'data': coldb.get(identifier)}, 200



api.add_resource(Collection, '/api/v1/collection/<string:identifier>')