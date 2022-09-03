from flask import Flask
import os
from flask import render_template, url_for, request
import pandas as pd

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

@app.route("/")
@app.route("/dashboard")
def dashboard():
    # load chart head
    head = ['Name', 'Age', 'Team', 'G', 'PA', 'AB', 'xAVG', 'xOBP', 'xSLG', 'xOPS', 'xHR', 'xK%', 'xBB%', 'xHR%', 'xBABIP', 'xISO', 'HBP', 'SF', 'xK', 'xBB', 'xEvents', 'xBIP', 'xH']

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
    return render_template("dashboard.html",head = head, stats = stats)

# @app.route("/stats/<pid>")
# def player(pid):
#     return pid

if __name__ == "__main__":

    # stats = pd.read_csv("CSV_files/xStats.csv")
    # stats = stats.sort_values(by=["xBB%"], ascending=False)
    # print(stats)
    port = int(os.environ.get("PORT",5100))
    app.run(debug=True, port=port)

