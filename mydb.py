import mysql.connector as mycont

database=mycont.connect(
   host='localhost',
   user='root',
   passwd='9a05101998',   
)
cursor=database.cursor()
cursor.execute("CREATE DATABASE myProject")