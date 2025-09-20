from flask import Flask
from flask_restful import Api
from models import db
from controller import LibraryResource, LibraryListResource

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

api.add_resource(LibraryListResource, '/api/library')
api.add_resource(LibraryResource, '/api/library/<string:isbn>')

if __name__ == '__main__':
    app.run(debug=True)