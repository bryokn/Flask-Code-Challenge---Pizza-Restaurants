from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.exc import IntegrityError
from flask import Flask

#initialize sqlalchemy
db = SQLAlchemy()

#define restaurant model
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade='all, delete-orphan')
    #validate restaurant name
    @validates('name')
    def validate_name(self, key, value):
        if len(value.split()) > 50:
            raise ValueError('Restaurant name must be less than 50 words')
        return value

    def __repr__(self):
        return f'<Restaurant {self.name}>'

#define the pizza model
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Pizza {self.name}>'

#define restaurant_pizza model
class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    #validate the price
    @validates('price')
    def validate_price(self, key, value):
        if value < 1 or value > 30:
            raise ValueError('Price must be between 1 and 30')
        return value

    def __repr__(self):
        return f'<RestaurantPizza {self.restaurant.name} - {self.pizza.name}>'