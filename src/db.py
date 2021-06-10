import psycopg2

connection = psycopg2.connect(dbname="mydb", user="postgres", password="postgres", host="localhost", port="5432")

cursor = connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS table2;''')

cursor.execute('''CREATE TABLE table2(
                    id INTEGER PRIMARY KEY,
                    completed BOOLEAN NOT NULL DEFAULT False,
                    creation_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
                  );
               ''')

sql_clause = 'INSERT INTO table2(id, completed) VALUES (%(id)s, %(completed)s);'
data = {'id':2, 'completed': False}

cursor.execute('INSERT INTO table2(id, completed) VALUES (%s, %s);', (1, True))
cursor.execute(sql_clause, data)

connection.commit()

connection.close()
cursor.close()
