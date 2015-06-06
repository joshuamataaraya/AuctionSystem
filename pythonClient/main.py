from flask import Flask
from flask import render_template
from sql import SQLConnection

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('userSelect.html')

if __name__ == "__main__":
    sqlCon = SQLConnection("autionDB", 'user', "123")
    con = sqlCon.connect()
    app.debug = True    #auto refresh
    app.run()
