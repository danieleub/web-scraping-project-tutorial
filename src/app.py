import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io
import random
import numpy as np
from bs4 import BeautifulSoup



url ="https://es.wikipedia.org/wiki/Caballeros_Reales_(Digimon)#:~:text=Los%20Caballeros%20Reales%20(%E3%83%AD%E3%82%A4%E3%83%A4%E3%83%AB%E3%83%8A%E3%82%A4%E3%83%84,la%20era%20mitol%C3%B3gica%20del%20Digimundo."
response = requests.get(url)

if response:
    sopa = BeautifulSoup(response.text, 'html')


html = io.StringIO(response.text)
tables = pd.read_html(html)
df = tables[1]




df.columns = ["Nombre USA", "Nombre original", "Katakana", "Origen"]
df['Poder'] = np.random.randint(100, 201, size=len(df))
df['Año debut'] = np.random.randint(2004, 2008, size=len(df))








conn = sqlite3.connect("digimon.db")

df.to_sql("royalknights", conn, if_exists="replace", index=False)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM royalknights")
print("Rows inserted:", cursor.fetchone()[0])

conn.commit()
conn.close()