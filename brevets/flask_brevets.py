"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import logging
import arrow  # Replacement for datetime, based on moment.js
import flask
from flask import request, render_template , redirect, url_for
from pymongo import MongoClient

import acp_times  # brevet time calculations
import config


app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

client = MongoClient(host="brevets_mongodb", port=27017)
db = client.breverstdb
collections=db['breverst']

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('brevets.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from km, using rules
    described at https://rusa.org/pages/acp-brevet-control-times-calculator.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    brevet_dist =request.args.get('brevet_dist',1000, type=int)
    begin_time = request.args.get('begin_time',type=str)
    begin_date = request.args.get('begin_date',type=str)
    open_time_field = request.args.get('open_time_field')
    close_time_field = request.args.get('close_time_field')
    date= begin_date+" "+begin_time




    app.logger.debug(f"request.args: {request.args}")
    app.logger.debug(f"km={km}")
    #app.logger.debug(f"open_time_field={open_time_field}")
    #app.logger.debug(f"close_time_field={close_time_field}")

    # FIXME: These probably aren't the right open and close times and brevets may be longer than 200km
    #   they need more arguments from the front-end.

    open_time = acp_times.open_time(km, brevet_dist,date)
    close_time = acp_times.close_time(km, brevet_dist,date)
    if km < 0:
        return render_template("error.html",
                               message="The control distance must be positive.")
    # الي كاتبه الدكتور
    #open_time = acp_times.open_time(km, 200, date)
    #close_time = acp_times.close_time(km, 200, date)

    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=='POST':
        km =(request.form.get('km'))
        dis = request.form.get('distance')
        op = request.form.get('open')
        cl = request.form.get('close')
        #جرب many و update
        item_sub = [{

            'brevets': dis,
            'km': km,
            'open': request.form['open'],
            'close': cl
        }]

        for item in item_sub:

           collections.insert_one(item)

        return redirect(url_for('index'))



@app.route("/display", methods=['GET','POST'])
def display():
    #_times = db.brevetsdb.find()
    _times=collections.find()
    times = [time for time in _times]
    return render_template('Display.html', times=times), 200

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.logger.info(f"Opening for global access on port {CONFIG.PORT}")
    app.run(port=CONFIG.PORT, host="0.0.0.0", debug=True)
