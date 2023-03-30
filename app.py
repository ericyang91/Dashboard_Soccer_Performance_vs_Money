# Import Dependencies
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData
from flask import Flask, jsonify, render_template
import psycopg2
import pandas as pd
from credentials import username, password

# Set up SQLAlchemuy engine and base to talk to the database
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost:5432/soccer_money")
Base = automap_base()
Base.prepare(autoload_with = engine)
data = Base.classes.all_leagues

# Set up Flask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('dash.html')

@app.route('/allleagues')
def allLeagues():
    session = Session(engine)
    countries = []
    query_country = session.query(data.country).distinct()
    countries = [sqlalchemyobject1[0] for sqlalchemyobject1 in query_country.all()]
    query_league = session.query(data.country, data.league).distinct()
    results = [(sqlalchemyobject2[0], sqlalchemyobject2[1] )for sqlalchemyobject2 in query_league.all()]
    return results

    # for league in (session.query(data.league).distinct().filter(data.country.in_(countries))):
    #     results.append(league)
    session.close()
    # print(results)
    # print('--------------')
    print(query)
    print('-------------')
    print(query.all)
    # leagues = list(np.ravel(results))
    
    # return jsonify(leagues)

# @app.route('/allclubs')
# def allClubs():
#     session = Session(engine)
#     results = []
#     for club in (session.query(data.club).distinct()):
#         results.append(club)
#     session.close()
    # print(results)
    # clubs = list(np.ravel(results))
    # print(clubs)
    # return jsonify(clubs)

@app.route("/alldata")
def allData():
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
    # all_teamsjson = jsonify(all_teams)

    # return all_teamsjson



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
