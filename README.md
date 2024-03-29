# Soccer: Is the Money Worth the Goals?
![soccer](https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/captures/soccer1.jpg)
## Purpose

The European soccer market has been increasing in size in the recent years. The level of increase is unprecedented, with multi-billionaires from countries like Qatar and Saudi Arabia taking ownership of the major clubs. The result is a hyper-inflation of player values.
This project uses bubble chart, bar chart, and a table to visualize the major European soccer league and their teams' monetary value and performance to see if there are any visible relationships between money and performance.
Leagues of interest include:
- Premier League (England)
- La Liga (Spain)
- Serie A (Italy)
- Bundesliga (Germany)
- Ligue 1 (France)
- Eredivisie (Netherlands)
- Liga Portugal (Portugal)
- Premier Liga (Russia)
- Super Lig (Turkiye)
- Jupiler League (Belgium)
- Bundesliga (Austria)

Note that the project is limited to visualization only. The relationship between the two factors must be further studied using correlation, regression, and/or machine learning.

## Data Preparation

[Data set](https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/data_scrape.ipynb) was prepared by scraping the most recent data from [Transfermarkt](https://www.transfermarkt.us/) using `BeautifulSoup`. The scraped data was cleaned and organized with `Pandas` and `Python`, which was then sent to `PostgreSQL` to be stored in a database. `SQLAlchemy` was used to retrieve the data from `PostgreSQL` and `Flask` was created for setting up the dashboard. The code is stored in [app.py](https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/app.py).

## Javascript Coding

`D3.js` and `Plotly` were used to create the bar chart, bubble chart, and league table. Both the `HTML` and the `Javascript code` are stored in [dash.html](https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/templates/dash.html). `CSS` code is stored in [main.css](https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/static/main.css).

## Dashboard

The dashboard composed of 5 different sections: Dropdown menu, Team Summary, Bubble Chart, 2 Bar Charts, and a League Table. Below is an overview of the dashboard.

![dashboard](https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/captures/dashfull.jpg)

There are two dropdown menus that allow users to select a league of interest and a club in the selected league.

<p align="center">
  <img src="https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/captures/dashboard.jpg" alt="menu"/>
</p>

The Team Summary side menu gives a summary of the club of selection. This summary includes the club's market value, total points in the league, average points per game, number of matches played, games won, games drawn, and games lost.

<p align="center">
  <img src="https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/captures/teamsummary.jpg" alt="summary"/>
</p>

The bubble chart gives users information of all the clubs in a league their market value, average points won per game, and the win-loss ratio. The size of the bubble depicts the market value.

<p align="center">
  <img src="https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/captures/bubblechart.jpg" alt="bubblechart"/>
</p>

There are two bar charts. The upper chart compares the market value between the selected club and the league average. The chart below compares the points won.

<p align="center">
  <img src="https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/captures/bar.jpg" alt="bar"/>
</p>

The league table shows a detailed value and performance information for all clubs in a league. Users can sort the different columns by clicking on the column headers.

<p align="center">
  <img src="https://github.com/ericyang91/Soccer_Is_the_Money_Worth_the_Goals/blob/main/captures/table.jpg" alt="table"/>
</p>

## Further Research

As noted above, this project is limited only to data visualization. Further research is required to analyze the relationship between money and performance. It would also be interesting to make comparison between the different leagues by using UEFA's club coefficients and the Champions League performance. Another nice addition to it would be to use tools such as the `Task Scheduler` to automate the process of updating the data set as the data on [Transfermarkt](https://www.transfermarkt.us/) gets updated.

## Libraries and Modules
[![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat)](https://pandas.pydata.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?logo=postgresql&logoColor=white&style=flat)](https://www.postgresql.org/)
[![pgAdmin](https://img.shields.io/badge/-pgAdmin-336791?logo=postgresql&logoColor=white&style=flat)](https://www.pgadmin.org/)
[![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white&style=flat)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-1C2833?logo=sqlalchemy&logoColor=white&style=flat)](https://www.sqlalchemy.org/)
[![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black&style=flat)](https://www.javascript.com/)
[![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?logo=plotly&logoColor=white&style=flat)](https://plotly.com/)
[![D3](https://img.shields.io/badge/-D3-F9A03C?logo=d3.js&logoColor=white&style=flat)](https://d3js.org/)
[![Beautiful Soup](https://img.shields.io/badge/BeautifulSoup-%E2%9C%A8-green)](https://pypi.org/project/beautifulsoup4/)

