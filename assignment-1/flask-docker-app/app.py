# Import Flask to create the app
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

@app.route("/")
def home():
    # This function will be called when the user visits the home page.
    return "Hello, Dockerized Flask App!"

# If this script is run directly, start the Flask app
if __name__ == "__main__":
     # Run the Flask app, making it accessible to all IPs and listening on port 5000
    app.run(host="0.0.0.0", port=5000)
