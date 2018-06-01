from __future__ import print_function
from flask import Flask, jsonify, request, render_template
import folium
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display
import os
from backhardcode2 import extract
from back import p
from ipywidgets import IntSlider

extract = extract()
p = p

app = Flask(__name__)

#countries = Country()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/countries', methods=['GET'])
def cunt():
	return render_template('countries.html', countries = extract)

@app.route('/population/', methods=['GET'])
def cuntry(id):
	return render_template('population.html', cunt = p)



@app.route('/population/<string:id>/', methods=['GET'])
def dis(id):
	return render_template('countries.html', id=id)


# @app.route('/lang', methods=['GET'])
# def returnALL():
#	return jsonify({'languages': languages})

# @app.route('/lang/<string:name>', methods=['GET'])
# def returnOne():
#	langs = [language for language in languages if language['name'] == name]
#	return jsonify({'language' : langs[0]})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
