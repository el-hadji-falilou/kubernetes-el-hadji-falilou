from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello_work():
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<p>Name : Falilou</p> <p>Project name : Challenge 1</p> <p>Version : V1</p> <p>Hostname : {hostname}</p> <p>Current date : {current_date}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)