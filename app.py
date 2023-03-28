# Import Dependencies
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
import psycopg2
from credentials import username, password
import pandas as pd

# Set up SQLAlchemuy engine and base
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost:5432/soccer_money")
Base = automap_base()
Base.prepare(autoload_with=engine)
data = Base.classes.concat


# Set up Flask
app = Flask(__name__)


@app.route("/")
def index():
  return (
        f"Welcome!<br/>"
        f"Available Routes:<br/>"
        f"/jsondata<br/>"
    )

@app.route("/jsondata")
def jsondata():
    session = Session(engine)
    results = session.query(data.club, data.country, data.league, data.market_value, data.pl, data.w, data.d, data.l, data.pts, data.pts_per_match).all()

    session.close()

    all_teams = []
    for club, country, league, market_value, pl, w, d, l, pts, pts_per_match in results:
        team_dict = {}
        team_dict["club"] = club
        team_dict["country"] = country
        team_dict["league"] = league
        team_dict["market_value"] = market_value
        team_dict["pl"] = pl
        team_dict["w"] = w
        team_dict["d"] = d
        team_dict["l"] = l
        team_dict["pts"] = pts
        team_dict["pts_per_match"] = pts_per_match
        all_teams.append(team_dict)

    return jsonify(all_teams)


# @app.route("/map")
# def map():
#     return render_template('map.html')

# @app.route("/chart")
# def chart():
#     return render_template('chart.html')

# @app.route("/pie")
# def pie():
#     return render_template('pie.html')

if __name__ == '__main__':
    app.run(debug=True)
