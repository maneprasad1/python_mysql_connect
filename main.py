import pandas as pd
from dotenv import load_dotenv
import os
import mysql.connector

# Load variables from .env
load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

# load excel file
df = pd.read_excel('leetcode_db.xlsx')
# change data types
df[['qno','srno']] = df[['qno','srno']].astype('int')
print(df.head())

cnx = mysql.connector.connect(user=db_user,
                              password=db_pass,
                              host=db_host,
                              database=db_name)
print("Connected to DB:", db_name)
cur = cnx.cursor()

cur.execute("""drop table leetcode""")

cur.execute("""create table leetcode(
            srno int primary key,
            qno int,
            question varchar(200),
            link varchar(300),
            level varchar(10),
            language varchar(10))""")
cnx.commit()

for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO leetcode (srno, qno, question, link, level, language) VALUES (%s, %s, %s, %s, %s, %s)",
        (row['srno'], row['qno'], row['question'], row['link'], row['level'], row['language'])
    )
cnx.commit()
cnx.close()