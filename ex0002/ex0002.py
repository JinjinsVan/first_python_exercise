import pymysql
import random

conn = pymysql.connect(host='localhost',user='root',password='root',db="codebook")
cursor = conn.cursor()
# #create db
# # cursor.execute('CREATE DATABASE codebook')

# #create table
createtableSQL = "CREATE TABLE Coupon(id int NOT NULL AUTO_INCREMENT, couponNum varchar(20) ,PRIMARY KEY(id))"
cursor.execute(createtableSQL)

# #delete table
# delTableSQL = "DROP TABLE Coupon"
# cursor.execute(delTableSQL)


#  # SQL insert  
#  insertSQL = "INSERT TABLE Coupon "
# # Execute the sqlQuery
# cursor.execute(sqlQuery)
# cursor.close()


couponSet = set()
while len(couponSet)<200:
	couponSet.add(random.randint(1000,9999))

conn = pymysql.connect(host='localhost',user='root',password='root',db='codebook')
cursor = conn.cursor()
insertSQL = 'INSERT INTO Coupon(couponNum) VALUES '
for coupon in couponSet:
	cursor.execute(insertSQL+'('+str(coupon)+')')

# cursor.close()
querySQL = 'SELECT * FROM Coupon'
cursor.execute(querySQL)
rows = cursor.fetchall()
for row in rows:
	print(row)

cursor.close()




