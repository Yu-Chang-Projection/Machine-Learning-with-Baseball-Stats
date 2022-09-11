from flask import Flask
import os, json
from flask import render_template, url_for, request, redirect
import pandas as pd

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

@app.route("/")
@app.route("/dashboard")
def dashboard():
    # load chart head
    head = ['Name', 'Age', 'Team', 'G', 'PA', 'AB', 'xAVG', 'xOBP', 'xSLG', 'xOPS', 'xHR', 'xK%', 'xBB%', 'AVG-xAVG',
            'OPS-xOPS', 'HR-xHR', 'xHR%', 'xBABIP', 'xISO', 'HBP', 'SF', 'xK', 'xBB', 'xEvents', 'xBIP', 'xH', 'AVG',
            'OBP', 'SLG', 'OPS', 'HR']
    # read stat file
    stats = pd.read_csv("xStats.csv")
    stats = stats[head]
    print(stats)
    # get filter
    sort_by = request.args.get('sort_by')
    direction = request.args.get('direction')
    ascending = False
    if direction == "asc":
        ascending = True
    if sort_by == None:
        stats = stats.sort_values(by=["xOPS"], ascending = ascending)
    else:
        stats = stats.sort_values(by=[sort_by], ascending = ascending)
    players = stats.iloc[:,0].to_list() # get all player names
    return render_template("dashboard.html",head = head, stats = stats, players = players)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ranks")
@app.route("/more")
@app.route("/link ")
def player():
    return render_template("soon.html")

@app.errorhandler(404)
def notfound(e):
    return render_template("notfound.html"),404

if __name__ == "__main__":

    # stats = pd.read_csv("CSV_files/Stats.csv")

    port = int(os.environ.get("PORT",5555))
    # app.run(debug=True, port=port) # local
    app.run(host='0.0.0.0', debug=False, port=port) # remote

