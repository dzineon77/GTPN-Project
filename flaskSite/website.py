#!/usr/bin/env python

import flask
import pandas as pd
# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html', name="index")


@APP.route('/login/')
def login():
    """ Displays the page greats who ever comes to visit it.
    """
    return flask.render_template('login.html', name="login")


@APP.route('/elements/')
def elements():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('elements.html')


@APP.route('/shop/')
def shopHome():
    fo = pd.read_csv(r"C:\Users\dzine\Downloads\MVP Data  - Sheet2.csv")
    shopUrls = fo['URLS']
    shopContactInfo = fo['ContactInfo']
    tempstorenames = []
    for i in range(len(fo['URLS'])):
        tempstorenames.append("StoreName{i}".format(i = i))
        
    return flask.render_template('shopHome.html', name = "shopHome", shopUrls = shopUrls, shopContactInfo = shopContactInfo, tempstorenames = tempstorenames)


@APP.route('/shop/<name>/')
def shop(name):
        
    storedesc = "Temporary store description here"
    images = None
    itemnames = ["item1", "item2", "item3", "item4", "item5", "item6"]
    itemprices = [1, 2, 3, 4, 5, 6]
    for i in range(len(itemprices)):
        itemprices[i] = str(itemprices[i])

    itemdesc = ["item1desc", "item2desc", "item3desc",
                "item4desc", "item5desc", "item6desc"]

    return flask.render_template('shop.html', name=name, storedesc=storedesc, itemnames=itemnames, itemprices=itemprices, itemdesc=itemdesc)


if __name__ == '__main__':
    APP.debug = True
    APP.run()
