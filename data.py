import sqlite3

db_path = "project.db"

# This function conencts to the DB and returns a conn and cur objects
def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# This function returns restaurant by their location
def read_Restaurants_by_location(location):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM Restaurants WHERE location = ?'
    value = location
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

# This function retrieves 1 pet by pet_id
def read_Restaurants_by_restaurant_ID(resto_ID):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM Restaurants WHERE ID = ?'
    value = resto_ID
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result

# This function inserts 1 pet data
def insert_Restaurants(resto_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO Restaurants (location, name, description, rating, food_type, image, price_range) VALUES (?,?,?,?,?,?,?)'
    values = (resto_data['location'], resto_data['name'],
              resto_data['description'], resto_data['rating'],
              resto_data['food_type'], resto_data['image'], resto_data['price_range'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

# This function updates a record
def update_Restaurants(resto_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE Restaurants SET location=?, name=?, description=?, rating=?, food_type=?, image=?, price_range=? WHERE ID=?"
    values = (resto_data['location'], resto_data['name'],
              resto_data['description'], resto_data['rating'],
              resto_data['food_type'], resto_data['image'],
              resto_data['price_range'], resto_data['ID'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_Restaurants(resto_ID):
    con, cur = connect_to_db(db_path)
    query = "DELETE FROM project.db WHERE ID=?"
    values = (resto_ID,)
    cur.execute(query, values)
    con.commit()
    con.close()

def search_Restaurants(query):
    conn, cur = connect_to_db(db_path)
    sql_query = "SELECT * FROM Restaurants WHERE name LIKE ? OR location LIKE ?"
    value = "%{}%".format(query)
    results = cur.execute(sql_query, (value, value)).fetchall()
    conn.close()
    return results