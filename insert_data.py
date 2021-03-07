import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="BJK2015bjk",
  database="IMDB"
)

file_path = "data/title.ratings.tsv"

data = pd.read_csv(file_path, sep='\t', header=0)

col_count = [len(l.split('\t')) for l in data.columns]
print(data.columns)
data.to_sql(con=mydb, name='table_name_for_df', if_exists='replace', flavor='mysql')


mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")