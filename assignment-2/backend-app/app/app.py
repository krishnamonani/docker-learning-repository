from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"))
    return conn

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        data = request.get_json()
        message = data.get('message')
        if message:
            try:
                cur.execute("INSERT INTO messages (message_text) VALUES (%s)", (message,))
                conn.commit()
                cur.close()
                conn.close()
                return jsonify({"status": "success", "message": "Message stored in database"}), 201
            except Exception as e:
                cur.close()
                conn.close()
                return jsonify({"status": "error", "message": str(e)}), 500

    elif request.method == 'GET':
        messages = []
        try:
            cur.execute("SELECT message_text FROM messages")
            rows = cur.fetchall()
            for row in rows:
                messages.append(row[0])
            cur.close()
            conn.close()
            return jsonify({"status": "success", "messages": messages}), 200
        except Exception as e:
            cur.close()
            conn.close()
            return jsonify({"status": "error", "message": str(e)}), 500

    # return '''<h1>Simple Backend App</h1>
    #         <p>Send a POST request with {"message": "your message"} to store data.</p>
    #         <p>Send a GET request to retrieve stored messages.</p>'''

    return '''<h1>Backend Application - Modified</h1>
        <p>Send a POST request with {"message": "your message"} to store data.</p>
        <p>Send a GET request to retrieve stored messages.</p>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)