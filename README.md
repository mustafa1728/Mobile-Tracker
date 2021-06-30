# Mobile-Tracker
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

## Todos

- [x] Build static routing map 
- [x] Add static tracking 
- [x] Add dynamic tracking
- [ ] Complete flask app
- [ ] Deploy flask app on heroku

