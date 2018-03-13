import MySQLdb as mdb
test_db = mdb.connect(host="localhost", user="root", passwd="admin", db="test_db", charset="utf8")
cursor = test_db.cursor()
cursor.execute("""drop table if exists person""")
cursor.execute("""
                create table person(
                    name    varchar(200), 
                    age     int, 
                    sex     varchar(20),
                    habit   varchar(200)
                )
               """)

cursor.execute("""
                insert into person(name, age, sex, habit) 
                values
                ("tom", 100, "male", "打球、看电影、读书") ;
               """)
cursor.execute("""
                insert into person(name, age, sex, habit) 
                values
                ("jerry", 500, "male", "打球、看电影、读书") ;
               """)

cursor.execute("""
                insert into person(name, age, sex, habit) 
                values
                ("lion", 600, "female", "打球、看电影、读书") ;
               """)
cursor.execute("""
                insert into person(name, age, sex, habit) 
                values
                ("tigger", 500, "male", "打球、看电影、读书") ;
               """)

cursor.execute("""
                insert into person(name, age, sex, habit) 
                values
                ("cat", 600, "female", "打球、看电影、读书") ;
               """)

test_db.commit()
# cursor.close()