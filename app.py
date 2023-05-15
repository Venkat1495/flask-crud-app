from flask import Flask, request, render_template, redirect, url_for
import pymysql
from sqlalchemy import create_engine

app = Flask(__name__)

# MySQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1:3307/flask-crud-app'

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


@app.route('/')
def index():
    # Show all MY Shows
    cursor.execute("SELECT * FROM MyShows")
    ITEMS = cursor.fetchall()
    print(ITEMS)
    return render_template('base.html', ITEMS = ITEMS)

@app.route("/delete/<int:show_id>")
def delete(show_id):
    print(show_id)
    # Delete one MY Show
    cursor.execute("DELETE FROM MyShows WHERE id = %s", show_id)
    mysql.commit()
    return redirect(url_for('index'))

# @app.route('/Add_a_Show', methods=["POST"])
# def Add_a_Show():
#     title = request.form.get("title")
#     director = request.form.get("director")
#     type = request.form.get("type")
#     anime = request.form.get("anime")
#     genre = request.form.get("genre")

#     cursor.execute('INSERT INTO MyShows (title, director, type, anime, genre) VALUES (%s, %s, %s, %s, %s)', (title, director, type, anime, genre))
#     mysql.commit()
#     message = "Form submitted successfully!"
#     return message

@app.route('/Add_a_Show')
def Add_form():
    return render_template('form.html')

if __name__ =="__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)