# Import required modules
import csv
import sqlite3
import os.path

import pandas as pd

url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
df = pd.read_csv(url,skiprows=[0])

df.to_csv('out.csv')


url = "https://archives.nseindia.com/products/content/sec_bhavdata_full_13042022.csv"
df = pd.read_csv(url,skiprows=[0])

df.to_csv('out2.csv')



connection = sqlite3.connect('BhavCopy.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE bhav(
				id INTEGER,
				SYMBOL TEXT,
	 			SERIES TEXT,
	 	 		DATE1 TEXT,
				PREV_CLOSE INTEGER,
				OPEN_PRICE INTEGER,	 
 				HIGH_PRICE INTEGER,
 					 LOW_PRICE INTEGER,	 
 					 LAST_PRICE INTEGER,	 
 					 CLOSE_PRICE INTEGER,	 
 					 AVG_PRICE INTEGER,	 
 					 TTL_TRD_QNTY INTEGER,	 
 					 TURNOVER_LACS INTEGER,	 
 					 NO_OF_TRADES INTEGER,	 
 					 DELIV_QTY INTEGER,
 					 DELIV_PER INTEGER
				)
				'''

# Creating the table into our
# database
cursor.execute(create_table)

# Opening the person-records.csv file
file2 = open('out2.csv')

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file2)

# SQL query to insert data into the
# person table
insert_records = "INSERT INTO bhav (id,SYMBOL,SERIES ,DATE1 ,PREV_CLOSE,OPEN_PRICE, HIGH_PRICE,	 LOW_PRICE	 ,LAST_PRICE,	 CLOSE_PRICE,	 AVG_PRICE,	 TTL_TRD_QNTY,	 TURNOVER_LACS,	 NO_OF_TRADES,	 DELIV_QTY,	 DELIV_PER) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM bhav"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
# for r in rows:
# 	print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()




# security Database 

# Connecting to the geeks database
connection=""

connection = sqlite3.connect('security.db')


cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE security(
				id INTEGER ,
				symbol TEXT NOT NULL,
				name TEXT ,
				series TEXT ,
				dates TEXT ,
				paid_up INTEGER, 
				market_lot INTEGER,
				isin_num TEXT ,
				face_val INTEGER

				)
				'''

# Creating the table into our
# database
cursor.execute(create_table)

# Opening the person-records.csv file
file = open('out.csv')

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)

# SQL query to insert data into the
# person table
insert_records = "INSERT INTO security (id,symbol ,name ,series,dates,paid_up,market_lot,isin_num,face_val) VALUES(?,?,?,?,?,?,?,?,?)"

# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM security"
rows = cursor.execute(select_all).fetchall()
connection.commit()

# closing the database connection
connection.close()

