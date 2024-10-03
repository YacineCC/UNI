import psycopg2 as psy


conn = psy.connect(database='dbdeyacine',host="localhost",port=5432, user='yacine', password='come01')

cur = conn.cursor()


cur.execute("""CREATE DOMAIN dom_sexe
   AS character(1)
   CHECK (VALUE IN ('M', 'F'));""")

cur.execute("""CREATE TABLE cours(
	id_cours integer primary key,
	danse varchar(10)
);""")

cur.execute("""INSERT INTO cours VALUES (1,'Salsa');
INSERT INTO cours VALUES (2,'Salsa');
INSERT INTO cours VALUES (3,'Rock');
INSERT INTO cours VALUES (4,'Rock');
INSERT INTO cours VALUES (5,'Rock');
INSERT INTO cours VALUES (6,'Tango');
INSERT INTO cours VALUES (7,'Tango');""")

conn.commit()

cur.close()
conn.close()
