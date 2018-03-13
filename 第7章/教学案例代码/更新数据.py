import MySQLdb as mdb
test_db = mdb.connect(host="localhost", user="root", passwd="admin", db="test_db", charset="utf8")
cursor = test_db.cursor()
cursor.execute("""
                update person
                set
                name = "史密斯",
                age = 50
               """)
test_db.commit()
cursor.close()