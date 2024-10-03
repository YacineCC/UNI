import psycopg2 as psy


conn = psy.connect(database='tp1',host="localhost",port=5432, user='yacine', password='TP1')

cur = conn.cursor()
cur.execute("""DROP SCHEMA PUBLIC CASCADE;""")
cur.execute("""CREATE SCHEMA PUBLIC;""")

cur.execute("""CREATE TABLE Departement(
   DID varchar(2), PRIMARY KEY(DID),
   Libelle varchar(20)
   );""")

cur.execute("""CREATE TABLE Employe(
        EID integer, PRIMARY KEY(EID),
        Nom varchar(20),
        DID varchar(2),
        CONSTRAINT fk_dept
            FOREIGN KEY(DID)
                REFERENCES Departement(DID)
        );""")


#cur.execute("""DROP TABLE IF EXISTS customers;
#DROP TABLE IF EXISTS contacts;""")
#
#cur.execute("""CREATE TABLE customers(
#   customer_id INT GENERATED ALWAYS AS IDENTITY,
#   customer_name VARCHAR(255) NOT NULL,
#   PRIMARY KEY(customer_id)
#);""")

#cur.execute("""CREATE TABLE contacts(
#   contact_id INT GENERATED ALWAYS AS IDENTITY,
#   customer_id INT,
#   contact_name VARCHAR(255) NOT NULL,
#   phone VARCHAR(15),
#   email VARCHAR(100),
#   PRIMARY KEY(contact_id),
#   CONSTRAINT fk_customer
#      FOREIGN KEY(customer_id)
#	  REFERENCES customers(customer_id)
#);""")

conn.commit()

cur.close()
conn.close()
