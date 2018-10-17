import os

from flask import Flask
from flask_restful import Api

from controller.item import ItemController, ItemListController
from controller.store import StoreController, StoreListController

app = Flask(__name__)

URL = 'postgres://dmqowcurvqleyf:5200c66b3bec9ca0e620804ba61a35047b3cf374cfaff589ca4ea199e1c807d4@ec2-54-83-11-247.compute-1.amazonaws.com:5432/da9o2ioierqh4i'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', URL)
app.config['SQLALCHEMY_TRACK_MODIFICATONS'] = False
api = Api(app)


@app.route('/')
def hello_world():
    return 'Minicourse - Web API with Python and Flask!'


api.add_resource(ItemController, '/item/<string:name>')
api.add_resource(ItemListController, '/items')
api.add_resource(StoreController, '/store/<string:name>')
api.add_resource(StoreListController, '/stores')

if __name__ == '__main__':
    from db import db

    db.init_app(app)


    @app.before_first_request
    def create_tables():
        db.create_all()


    app.run(host='0.0.0.0', debug=True, port=80)