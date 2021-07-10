# Mobile-Tracker

<a href="https://mysterious-woodland-91712.herokuapp.com"><img alt="Flask" src="https://img.shields.io/badge/flask-%23575.svg?style=for-the-badge&logo=flask"/></a>

Modelling mobile network communication hierarchy and simulating mobile location tracking.


This is a simple python-based implementation for simulating mobile tracking. A detailed Problem statement can be found [here](./Problem-Statement.pdf)

## Instructions for use

Clone the repo and open a terminal inside this folder. 

Add/change an [actions](./actions/) file according to what actions you want to perform in the routing map. Follow the [format](./actions/format.txt) provided.

After that, simple run `main.py` with path of the actions file:

Example usage:
~~~
python3 main.py --actions actions/actions1.txt
~~~

## App

The app is being deployed on heroku. It should show up [here](https://mysterious-woodland-91712.herokuapp.com).

