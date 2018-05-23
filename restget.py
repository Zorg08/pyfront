from __future__ import print_function
from flask import Flask, jsonify, request, render_template
import folium
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display
import os
import backhardcode as hc

dat = hc.exit


app = Flask(__name__)


def f(population):
	return population

interact(f, population=10);

@app.route('/', methods=['POST'])
def newtest():
	return f()

@app.route('/', methods=['GET'])
def test():

	return jsonify({'message': dat})

@app.route('/lang', methods=['GET'])
def returnALL():
	return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne():
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

if __name__ == '__main__':
	app.run(debug=True, port=8080)
