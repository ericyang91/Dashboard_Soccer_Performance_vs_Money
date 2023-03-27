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
data = Base.classes.all_leagues

# Set up Flask
app = Flask(__name__)


# @app.route("/")
# # def index():
#     # return render_template('index.html')

# @app.route("/jsondata")
# def jsondata():
#     session = Session(engine)
#     results = session.query(bundesliga.club).all()

#     session.close()

#     all_teams = []
#     for country, league_id, league, team, average_age, currency, market_value, lat, long, rk, mp, w, d, l, gf, ga, gd, pts, pts_per_match in results:
#         team_dict = {}
#         team_dict["country"] = country
#         team_dict["league_id"] = league_id
#         team_dict["league"] = league
#         team_dict["team"] = team
#         team_dict["average_age"] = average_age
#         team_dict["currency"] = currency
#         team_dict["market_value"] = market_value
#         team_dict["lat"] = lat
#         team_dict["long"] = long
#         team_dict["rk"] = rk
#         team_dict["mp"] = mp
#         team_dict["w"] = w
#         team_dict["d"] = d
#         team_dict["l"] = l
#         team_dict["gf"] = gf
#         team_dict["ga"] = ga
#         team_dict["gd"] = gd
#         team_dict["pts"] = pts
#         team_dict["pts_per_match"] = pts_per_match
#         all_teams.append(team_dict)

#     return jsonify(all_teams)


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
