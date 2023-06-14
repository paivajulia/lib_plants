import mechanicalsoup
import pandas as pd
import sqlite3

#to find and extract maranta
browser_maranta = mechanicalsoup.StatefulBrowser()
browser_maranta.open("https://en.wikipedia.org/wiki/Maranta_(plant)")
species_maranta=browser_maranta.page.find_all("a", attrs={"class":"new"})
maranta = [value.text for value in species_maranta]
maranta = maranta[:12]
#print(maranta)

#to find and extract hoya
browser_hoya = mechanicalsoup.StatefulBrowser()
browser_hoya.open("https://en.wikipedia.org/wiki/Hoya_(plant)")
species_hoya=browser_hoya.page.find_all("a")
hoya = [value.text for value in species_hoya]
hoya = hoya[150:163]
hoya = hoya [:12]
#print(hoya)

# to find and extract peperomia
browser_peperomia = mechanicalsoup.StatefulBrowser()
browser_peperomia.open("https://en.wikipedia.org/wiki/Peperomia")
species_peperomia=browser_peperomia.page.find_all("a")
peperomia = [value.text for value in species_peperomia]
"""print(peperomia.index("Peperomia argyreia"))
print(peperomia.index("Peperomia tetraphylla"))"""
peperomia = peperomia[305:321]
peperomia = peperomia[:12]
#print(peperomia)

# to create a dictionary
dict_plant = {
    "Maranta":maranta,
    "Hoya":hoya,
    "Peperomia":peperomia
}


# create new database and cursor
connection = sqlite3.connect("plants_new.db")
cursor = connection.cursor()

# create database table and insert all data
df = pd.DataFrame(data=dict_plant)
name_table = "plants"
df.to_sql(name_table, connection, if_exists= "replace", index=False)

# PERMANENTLY save inserted data in "plants_new"
connection.commit()

connection.close()

