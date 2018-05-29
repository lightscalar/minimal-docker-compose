from flask import Flask
from pymongo import MongoClient


# Connect to MongoDB, just to show we can
users = MongoClient("mongodb-1", 27017).demo.users

# Define server app.
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hey, we have Flask in a Docker container!"


if __name__ == "__main__":
    print("RUNNING NOW.")
    app.run(debug=True, host="0.0.0.0", port=3000)
