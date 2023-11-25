from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    display_file = open("noticeable.txt","r")
    complete = ""
    for line in display_file:
        complete+=line
        complete+="\n"
    return complete