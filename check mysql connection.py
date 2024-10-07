import MySQLdb

# Replace with your actual MySQL credentials
db = MySQLdb.connect(host='localhost', user='your_username', passwd='your_password', db='manage')

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version: {}".format(data))

db.close()
