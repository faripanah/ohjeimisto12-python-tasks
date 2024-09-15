import mysql.connector 

def hae_icaokoodi(koodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{koodi}'"
    kursori = yhteys.cursor(dictionary= True)
    kursori.execute(sql)
    tulos = kursori.fetchone()
    print(tulos)
    return


yhteys = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "fari1359",
    database = "flight_game",
    autocommit = True

)
koodi = (input("Syötä lentoaseman ICAO-koodin: "))
hae_icaokoodi(koodi)
