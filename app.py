from flask import Flask, request, jsonify
import pymysql
import os
from sqlalchemy import create_engine

app = Flask(__name__)

# MySQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1:51559/flask-crud-app'

# Create SQLAlchemy engine
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Create pymysql connection
mysql = pymysql.connect(
    host=engine.url.host,
    port=engine.url.port,
    user=engine.url.username,
    password=engine.url.password,
    db=engine.url.database
)

#************IMP INFO*****************
# HOST="aws.connect.psdb.cloud"
# USERNAME="mtcvbf1one39c8kpl112"
# PASSWORD="pscale_pw_M6L8nuznl6Xr3zbtR7GBUJm5vhMcGZ5YbZK4wVoRGdS"
# DATABASE="flask-crud-app"

# Opened cursor to execute MySQL quiries 
cursor = mysql.cursor()

# check if MySQL connection is successful
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)


