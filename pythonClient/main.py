from flask import Flask
from sql import SQLConnection

app = Flask(__name__)

@app.route("/")
def hello():
    return "Db connected"

if __name__ == "__main__":
    sqlCon = SQLConnection("autionDB", 'user', "123")
    con = sqlCon.connect()
    app.debug = True    #auto refresh
    app.run()
