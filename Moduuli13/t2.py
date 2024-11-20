from flask import Flask, jsonify
import mysql.connector

# Connect to the database
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="rahtipeli",
    user="root",
    password="fari1359",
    autocommit=True,
    collation='utf8mb4_unicode_ci'
)

app = Flask(__name__)

@app.route('/kenttä/<ident>')
def kenttä(ident):
    # SQL query to get the airport details
    sql = """
    SELECT airport.name, airport.municipality, country.name 
    FROM airport 
    JOIN country ON airport.iso_country = country.iso_country 
    WHERE airport.ident = %s;
    """
    kursori = yhteys.cursor()
    kursori.execute(sql, (ident,))
    tulos = kursori.fetchone()

    # If a matching airport is found
    if tulos:
        vastaus = {
            "ICAO": ident,
            "Name": tulos[0],
            "Municipality": tulos[1],
            "Country": tulos[2]
        }
    else:
        vastaus = {
            "Error": "Airport not found",
            "ICAO": ident
        }

    return jsonify(vastaus)

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)









