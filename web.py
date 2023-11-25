from flask import Flask
from flask import send_file
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    display_file = open("display.txt", "r")
    data = []
    for line in display_file:
        data.append(line)
    index_file = open("index.txt", "r")
    index = index_file.readline()
    display_file.close()

    print(data)

    if data[0] == "-1\n":
        return render_template("display_end_template.html",
                               index=data[1],es = data[2],ms = data[3])

    return render_template("display_template.html",
                           index=index, noticed_index=data[4], resulting_index=data[3])


@app.route("/data/<filename>")
def seek_data(filename):
    return send_file(filename)
