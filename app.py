from flask import Flask, request, jsonify
import pymysql
import os

#************IMP INFO*****************
# HOST="aws.connect.psdb.cloud"
# USERNAME="mtcvbf1one39c8kpl112"
# PASSWORD="pscale_pw_M6L8nuznl6Xr3zbtR7GBUJm5vhMcGZ5YbZK4wVoRGdS"
# DATABASE="flask-crud-app"

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USERNAME')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DATABASE')

mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)


# check if MySQL connection is successful
cursor = mysql.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)