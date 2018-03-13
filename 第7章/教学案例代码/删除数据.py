cursor = test_db.cursor()
cursor.execute("delete from person where age = '500'")
test_db.commit()
cursor.close()