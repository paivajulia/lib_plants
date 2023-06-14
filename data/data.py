import sqlite3
import pandas as pd

#create a database
connection = sqlite3.connect("plants.db")

#communicate with the database
cursor = connection.cursor()
cursor.execute("create table plants (release_family text, release_name text, light text)")


#data to be insert into the database
release_list = [
    ("Hoya", "Princess cavernosa", "Low"),
    ("Maranta", "Triosatr", "Low"),
    ("Peperomia", "Obtusifolia 'Marble", "Low"),
    ("Peperomia", "Caperata Frost", "Low"),
    ("Peperomia", "Argyreia", "Low"),
    ("Cactus", "Gymnocalycium anisitsii subsp. Damsii", "High"),
    ("Maranta", "leuconeura var. Erythroneura", "Low"),
    ("Jiboia", "Epiperium", "Low")
]  
toxic_list = [
    ("Hoya", "No"),
    ("Maranta", "No"),
    ("Peperomia", "No"),
    ("Cactus", "No"),
    ("Jiboia", "Yes")
]  



cursor.executemany("insert into plants values (?,?,?)", release_list)


#print database rows
for row in cursor.execute("select * from plants"):
    print(row)

# print specific rows from the plants table
print("******************************")
cursor.execute("select * from plants where light=:l", {"l": "High"})
plants_search = cursor.fetchall()
print(plants_search)

#to create a new table
cursor.execute("create table toxicCats (plants_release_family text, toxic text)")
cursor.executemany("insert into toxicCats values (?,?)", toxic_list)
# to saving changes immediatley
connection.commit()

#to select only teh rows where toxicCats_toxic=No
cursor.execute("select * from toxicCats where toxic=:t", {"t": "No"})
toxicCats_searche = cursor.fetchall()
print(toxicCats_searche)

#to combine data from 2 tables and manipulate it
cursor.execute("select plants.*, toxicCats.* from plants inner join toxicCats on plants.release_family = toxicCats.plants_release_family")
df = pd.DataFrame(cursor.fetchall())
print (df)




connection.close()