from flask import Flask, jsonify, make_response
import mysql.connector


app = Flask(__name__)

@app.route("/", methods=['GET'])
def give_data():
    connection = mysql.connector.connect(user='root', password='root12', host='db', port='3306', database='db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM people")
    result = cursor.fetchall()
    feedback = dict(result)
    return make_response(jsonify(feedback), 200)

@app.route("/health", methods=['GET'])
def health():
    return make_response(jsonify({"status": "OK"}), 200)

@app.errorhandler(404)
def page_not_found(e):
    return make_response("<p>404 not found</p>", 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
