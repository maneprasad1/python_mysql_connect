import pandas as pd
import mysql.connector
# load excel file
df = pd.read_excel('leetcode_db.xlsx')
# change data types
df[['qno','srno']] = df[['qno','srno']].astype('int')
print(df.head())

cnx = mysql.connector.connect(user='root',
                              password='PrasadM@2003',
                              host='127.0.0.1',
                              database='leetcode')

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