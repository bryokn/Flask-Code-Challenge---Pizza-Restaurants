#import modules
from flask import Flask, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate

#initialize flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

#route to get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    print("get_restaurants route called")
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address, } for r in restaurants])

#route to get a specific restaurant by ID
@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    print(f"get_restaurant route called with restaurant_id: {restaurant_id}")
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        print("Restaurant not found")
        return jsonify({'error': 'Restaurant not found'}), 404
    
    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas':[{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.restaurant_pizzas]        
    })

#route to delete restaurant by ID
@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    print(f"delete_restaurant route called with restaurant_id: {restaurant_id}")
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        print("Restaurant not found")
        return jsonify({'error': 'Restaurant not found'}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    print("Restaurant deleted")
    return '', 204

#route to get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    print("get_pizzas route called")
    pizzas = Pizza.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas])

#route to create a restaurant pizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    print("create_restaurant_pizza route called")
    data = request.get_json()
    restaurant_pizza = RestaurantPizza(
        price=data['price'],
        restaurant_id=data['restaurant_id'],
        pizza_id=data['pizza_id']
    )
    
    try:
        db.session.add(restaurant_pizza)
        db.session.commit()
        print("Restaurant pizza created")
    except IntegrityError as e:
        db.session.rollback()
        print("Validation error occurred")
        return jsonify({'errors': ['Validation errors']}), 422
    
    pizza = Pizza.query.get(data['pizza_id'])
    return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients})

#run the application
if __name__ =='__main__':
    print("Running Flask Application")
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)