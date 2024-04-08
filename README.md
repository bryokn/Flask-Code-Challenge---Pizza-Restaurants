# Flask-Code-Challenge - Pizza-Restaurants
This is a Flask-based API for managing restaurants, pizzas, and the relationship between them (RestaurantPizza).

## Features
- Get a list of all restaurants
- Get details of a specific restaurant, including the pizzas available
- Delete a restaurant
- Get a list of all pizzas
- Create a new relationship between a restaurant and a pizza

## Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

The API will be available at `http://127.0.0.1:5555`

## API Endpoints
### GET /restaurants
- Return a list of all restaurants.
### Get /restaurants/<int:restaurant_id>
- Returns details of a specific restaurant, including the pizzas available.

### DELETE /restaurants/<int:restaurant_id>
- Deletes a specific restaurant.

### GET /pizzas
- Returns a list of all pizzas.

### POST /restaurant_pizzas
- Creates a new relationship between a restaurant and a pizza.

## Code Breakdown

1. **app.py**:
- Imports the necessary modules and initializes the Flask application.
- Defines the API routes and their corresponding functions.
- Handles CRUD operations for restaurants, pizzas, and the relationship between them.

2. **models.py**:
- Defines the database models for `Restaurant`, `Pizza`, and `RestaurantPizza`.
- Includes validation logic for the `name` and `price` fields.

3. **seed.py**:
- Populates the database with initial data for restaurants and pizzas.
- Creates some sample relationships between restaurants and pizzas.

## License

This project is licensed under the [MIT License](LICENSE).