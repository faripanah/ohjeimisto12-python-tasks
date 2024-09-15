import mysql.connector 

def laske_lentokentatyypi_maara(koodi):
    sql = f"SELECT count(*), type FROM airport WHERE iso_country = %s GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
         for rivi in tulos:
             print(f"{rivi[1]}  {rivi[0]} kpl.")
    else:
        print("Lentokenttiä ei löytynyt.")

    return
    

yhteys = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "fari1359",
    database = "flight_game",
    autocommit = True

)

maakoodi = input("Syötä maa koodin: ")
print(f"Maassa {maakoodi} olevat lentokenttätyypit: ")
laske_lentokentatyypi_maara(maakoodi)

   
