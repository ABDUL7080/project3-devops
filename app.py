from flask import Flask
import socket
import datetime
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='/app/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.route("/")
def home():
    logging.info("Homepage visited")
    return "🚀 Project 3 - System Info App details Abjjdull  shaikh"

@app.route("/info")
def info():
    logging.info("Info endpoint accessed")
    return {
        "hostname": socket.gethostname(),
        "version": "3.0",
        "time": str(datetime.datetime.now())
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)