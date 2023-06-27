import sqlite3

db_path = "project.db"

# This function conencts to the DB and returns a conn and cur objects
def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# This function returns restaurant by their location
def read_restaurant_by_location(location):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM Restaurants WHERE location = ?'
    value = location
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

# This function retrieves 1 pet by pet_id
def read_restaurant_by_restaurant_id(resto_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM Restaurants WHERE id = ?'
    value = resto_id
    result = cur.execute(query,(value,)).fetchall()
    conn.close()
    return result

# This function inserts 1 pet data
def insert_restaurant(resto_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO Restaurants (location, name, description, rating, food_type, image, price_range) VALUES (?,?,?,?,?,?,?)'
    values = (resto_data['location'], resto_data['name'],
              resto_data['description'], resto_data['rating'],
              resto_data['food_type'], resto_data['image'], resto_data['price_range'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

# This function updates a record
def update_restaurant(resto_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE Restaurants SET location=?, name=?, description=?, rating=?, food_type=?, image=?, price_range=? WHERE ID=?"
    values = (resto_data['location'], resto_data['name'],
              resto_data['description'], resto_data['rating'],
              resto_data['food_type'], resto_data['image'],
              resto_data['price_range'], resto_data['ID'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_restaurant(resto_id):
    con, cur = connect_to_db(db_path)
    query = "DELETE FROM project.db WHERE ID=?"
    values = (resto_id,)
    cur.execute(query, values)
    con.commit()
    con.close()

