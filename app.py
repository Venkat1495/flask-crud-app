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


# Why below line ?
@app.route('/shows', methods=['GET'])
def get_shows():
    cursor.execute("SELECT * FROM MyShows")
    shows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    results = []
    # little more explanation on below line ?
    for show in shows:
        results.append(dict(zip(columns, show)))
    return jsonify(results)


@app.route('/shows/<int:show_id>', methods=['GET'])
def get_show(show_id):
    cursor.execute("SELECT * FROM MyShows WHERE id = %s", (show_id,))
    show = cursor.fetchone()
    if show is None:
        return jsonify({'error': 'Show not found'}), 404
    columns = [column[0] for column in cursor.description]
    result = dict(zip(columns, show))
    return jsonify(result)


@app.route('/shows', methods=['POST'])
def create_show():
    data = request.json
    title = data['title']
    director = data.get('director', None)
    show_type = data['type']
    anime = data['anime']
    genre = data.get('genre', None)
    insert_query = "INSERT INTO MyShows (title, director, type, anime, genre) VALUES (%s, %s, %s, %s, %s)"
    values = (title, director, show_type, anime, genre)
    cursor.execute(insert_query, values)
    # little more explanation on below line ?
    mysql.commit()
    return jsonify({'message': 'Show created successfully'}), 201


@app.route('/shows/<int:show_id>', methods=['PUT'])
def update_show(show_id):
    data = request.json
    title = data['title']
    director = data.get('director', None)
    show_type = data['type']
    anime = data['anime']
    genre = data.get('genre', None)
    update_query = "UPDATE MyShows SET title = %s, director = %s, type = %s, anime = %s, genre = %s WHERE id = %s"
    values = (title, director, show_type, anime, genre, show_id)
    cursor.execute(update_query, values)
    mysql.commit()
    return jsonify({'message': 'Show updated successfully'})


@app.route('/shows/<int:show_id>', methods=['DELETE'])
def delete_show(show_id):
    delete_query = "DELETE FROM MyShows WHERE id = %s"
    cursor.execute(delete_query, (show_id,))
    mysql.commit()
    return jsonify({'message': 'Show deleted successfully'})


if __name__ == '__main__':
    app.run()