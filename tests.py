from flask import Flask

app = Flask(__name_)

@app.route("/")
def index():
   return "Hellow from DW"
