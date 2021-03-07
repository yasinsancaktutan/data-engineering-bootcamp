import pandas as pd

# Loading data from tsv files
title_akas = pd.read_csv('data/title.akas.tsv', delimiter='\t',index_col=False)
title_basic = pd.read_csv('data/title.basic.tsv', delimiter='\t',index_col=False)
title_crew = pd.read_csv('data/title.crew.tsv', delimiter='\t',index_col=False)
title_episode = pd.read_csv('data/title.episode.tsv', delimiter='\t',index_col=False)
title_principals = pd.read_csv('data/title.principals.tsv', delimiter='\t',index_col=False)
title_ratings = pd.read_csv('data/title.ratings.tsv', delimiter='\t',index_col=False)
name_basics = pd.read_csv('data/name.basics.tsv', delimiter='\t',index_col=False)

# replacing \\N with None
title_akas = title_akas.replace('\\N', None)
title_basic = title_basic.replace('\\N', None)
title_crew = title_crew.replace('\\N', None)
title_episode = title_episode.replace('\\N', None)
title_principals = title_principals.replace('\\N', None)
title_ratings = title_ratings.replace('\\N', None)
name_basics = name_basics.replace('\\N', None)

import mysql.connector as msql
from mysql.connector import Error

# create database (if not exists)
try:
    conn = msql.connect(host='localhost', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute('DROP DATABASE IF EXISTS imdb;')
        cursor.execute("CREATE DATABASE imdb")
        print("imdb database is created")

except Error as e:
    print("Error while connecting to MySQL", e)

try:
    conn = msql.connect(host='localhost', database='imdb', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS title_akas;')
        print('Creating table title_akas....')

        cursor.execute("CREATE TABLE title_akas (titleId text null,ordering int null,title text null,region text null,"
                       "language text null,types text null,attributes text null,isOriginalTitle int null) ")
        print("title_akas table is created....")

        cursor.execute('DROP TABLE IF EXISTS title_basic;')
        print('Creating table title_basic....')

        cursor.execute("create table title_basic (tconst text null,titleType text null,primaryTitle text null,"
                       "originalTitle text null,isAdult int null,startYear int null,endYear int null,runtimeMinutes int null,"
                       "genres text null)")
        print("title_basic table is created....")

        cursor.execute('DROP TABLE IF EXISTS title_crew;')
        print('Creating table title_crew....')

        cursor.execute("create table title_crew (tconst text null,directors text null,writers text null)")
        print("title_crew table is created....")

        cursor.execute('DROP TABLE IF EXISTS title_episode;')
        print('Creating table title_episode....')

        cursor.execute("create table title_episode (tconst text null,parentTconst text null,seasonNumber int null,episodeNumber int null)")
        print("title_episode table is created....")

        cursor.execute('DROP TABLE IF EXISTS title_principals;')
        print('Creating table title_principals....')

        cursor.execute("create table title_principals (tconst text null,ordering int null,nconst text null,category text null,"
                       "job text null,characters text null)")
        print("title_principals table is created....")

        cursor.execute('DROP TABLE IF EXISTS title_ratings;')
        print('Creating table title_ratings....')

        cursor.execute("create table `title.ratings` (tconst text null,averageRating double null,numVotes int null);")
        print("title_ratings table is created....")

        cursor.execute('DROP TABLE IF EXISTS name_basics;')
        print('Creating table name_basics....')

        cursor.execute("create table name_basics(nconst text null,primaryName text null,birthYear int null,deathYear int null,"
                       "primaryProfession text null,knownForTitles text null);")
        print("name_basics table is created....")

        # inserting values to tables
        for i,row in title_akas.iterrows():
            sql = "INSERT INTO imdb.title_akas VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()

        for i,row in title_basic.iterrows():
            sql = "INSERT INTO imdb.title_basic VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()

        for i,row in title_crew.iterrows():
            sql = "INSERT INTO imdb.title_crew VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()

        for i,row in title_episode.iterrows():
            sql = "INSERT INTO imdb.title_episode VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()

        for i,row in title_principals.iterrows():
            sql = "INSERT INTO imdb.title_principals VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()

        for i,row in title_ratings.iterrows():
            sql = "INSERT INTO imdb.title_ratings VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()

        for i,row in name_basics.iterrows():
            sql = "INSERT INTO imdb.name_basics VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()

        print("records inserted....")

except Error as e:
    print("Error while connecting to MySQL", e)