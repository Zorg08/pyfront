from __future__ import print_function
from flask import Flask, jsonify, request, render_template
import folium
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display
import os
from backhardcode2 import extract
from back import country_population, countryss
from back import country_popu

from ipywidgets import IntSlider

extract = extract()
country_population = country_population
country_popu = country_popu
countryss = countryss


app = Flask(__name__)

#countries = Country()

#main
@app.route('/')
def home():
    return render_template('index.html')

#list of country
@app.route('/country', methods=['GET'])
def listing():
	return render_template('countries.html', countries = extract)


#population 2013
@app.route('/countries2013', methods=['GET'])
def cunta():
	return render_template('2013.html', countries = country_population)

#population 2015
@app.route('/countries2015', methods=['GET'])
def cunti():
	return render_template('2015.html', countries = countryss)

#population 2018
@app.route('/countries2018', methods=['GET'])
def cunt():
	#return jsonify({'countries' : country_popu})
	return render_template('2018.html', countries = country_popu)	





#@app.route('/population/<string:id>/', methods=['GET'])
#def dis(id):
#	return render_template('countries.html', id=id)


# @app.route('/lang', methods=['GET'])
# def returnALL():
#	return jsonify({'languages': languages})

# @app.route('/lang/<string:name>', methods=['GET'])
# def returnOne():
#	langs = [language for language in languages if language['name'] == name]
#	return jsonify({'language' : langs[0]})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
