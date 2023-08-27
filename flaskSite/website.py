#!/usr/bin/env python

import flask
import pandas as pd
# Create the application.
APP = flask.Flask(__name__)

fo = pd.read_csv(r"C:\Users\dzine\Downloads\MVP Data  - Sheet2.csv")
shopUrls = fo['URLS']
shopContactInfo = fo['ContactInfo']

dict = {}
for i in range(len(shopUrls)):
    dict[shopUrls[i].lstrip("https://")] = shopContactInfo[i]


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

    tempstorenames = []
    for i in range(len(fo['URLS'])):
        tempstorenames.append(shopUrls[i].lstrip("https://"))

    return flask.render_template('shopHome.html', name="shopHome", shopUrls=shopUrls, shopContactInfo=shopContactInfo, tempstorenames=tempstorenames)


@APP.route('/shop/<name>/')
def shop(name):

    images = None
    itemnames = ["item1", "item2", "item3", "item4", "item5", "item6"]
    itemprices = [1, 2, 3, 4, 5, 6]
    for i in range(len(itemprices)):
        itemprices[i] = str(itemprices[i])

    itemdesc = ["item1desc", "item2desc", "item3desc",
                "item4desc", "item5desc", "item6desc"]

    shopContactInfo = dict[name + "/"]

    return flask.render_template('shop.html', name=name, shopContactInfo=shopContactInfo, itemnames=itemnames, itemprices=itemprices, itemdesc=itemdesc)


if __name__ == '__main__':
    APP.debug = True
    APP.run()
