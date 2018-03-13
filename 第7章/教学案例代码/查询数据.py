# ... 连接数据库等操作同上... 
cursor = test_db.cursor()
cursor.execute("""
                select * from person
               """)
result = cursor.fetchone()   # 取一条数据
print(result)

print("-"*10)
result = cursor.fetchmany(2)  # 取两条
for row in result:
    print("每一行数据类型：%s" % str(type(row)) )
    print(row[0], row[1], row[2]) # 获得每行的第一个、第二个、第三个属性。
print("-"*10)

result = cursor.fetchall()
for row in result:
    print(row[0], row[1], row[2], row[3])

cursor.close()