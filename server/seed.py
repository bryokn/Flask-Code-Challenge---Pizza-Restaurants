#import necessary modules
from app import app, db, Restaurant, Pizza, RestaurantPizza

#create sample data within app context
with app.app_context():
    #create 2 restaurants
    restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
    restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')
    #create 2 pizza types
    pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
    #add the restaurants and pizzas to the db
    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2])
    db.session.commit()
    #create associations btw restaurants and pizzas
    restaurant_pizza1 = RestaurantPizza(price=5, restaurant_id=1, pizza_id=1)
    restaurant_pizza2 = RestaurantPizza(price=7, restaurant_id=1, pizza_id=2)
    restaurant_pizza3 = RestaurantPizza(price=8, restaurant_id=2, pizza_id=2)
    #add associations to the database
    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()