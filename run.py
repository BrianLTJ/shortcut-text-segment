from flask import Flask
from app import app

DEBUG = True
PORT = 5000
HOST = "0.0.0.0"

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
