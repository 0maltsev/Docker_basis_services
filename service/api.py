from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'products': ['product_1', 'product_2', 'product_3', 'product_4']
        }

# Create routes
api.add_resource(Product, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)