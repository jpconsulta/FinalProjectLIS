from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('kami.html')

@app.route('/locations/<location>') #read_pets_by_pet_type so yung first val ng SQL siguro
def restaurant(location):
    restaurant_SQLlist = read_Restaurants_by_location(location)
    return render_template("locations.html", location_template=location, restaurant_template=restaurant_SQLlist) #lahat ng may template ilalagay sa html {{ }}

@app.route('/restaurants/<int:restaurant_ID>')
def restaurant_name(restaurant_ID):
    restaurant_identification= read_Restaurants_by_restaurant_ID(restaurant_ID)
    return render_template("restaurants.html",identification_template=restaurant_identification) 

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processed', methods=['post'])
def processing():
    Restaurants_data = {
        "location": request.form['location'],
        "name": request.form['restaurant_name'],
        "description": request.form['restaurant_description'],
        "rating": request.form['restaurant_rating'],
        "food_type": request.form['restaurant_foodtype'],
        "image": request.form['restaurant_url'],
        "price_range": request.form['restaurant_price_range']
    }
    insert_Restaurants(Restaurants_data)
    return redirect(url_for('restaurant', location=request.form['location']))

@app.route('/modify', methods=['post'])
def modify():
    
    if request.form["modify"] == "edit":
       
        resto_id = request.form["resto_id"] 
        resto_id = read_Restaurants_by_restaurant_ID(resto_id)
      
        return render_template('update.html', restaurant=restaurant)
    
    elif request.form["modify"] == "delete":
        return render_template('index.html')
       
    

@app.route('/update', methods=['post'])
def update():
    resto_data = {
        "restaurant_id" : request.form["ID"],
        "location": request.form['location'],
        "name": request.form['name'],
        "description": request.form['description'],
        "rating": request.form['rating'],
        "foodtype": request.form['food_type'],
        "image": request.form['image'],
        "price_range": request.form['price_range']
    }
    update_Restaurants(resto_data)
    return redirect(url_for('Restaurants',restaurant_ID = request.form['ID']))

@app.route('/search', methods=['get'])
def search():
    query = request.args.get('query', '')
    results = search_Restaurants(query)
    return render_template('searchpage.html', query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)