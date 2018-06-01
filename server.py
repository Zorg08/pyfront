import os
import socket
from flask import Flask
from flask import request
from flask import send_from_directory
from github_analysis import make_me


app = Flask(__name__)


@app.route("/")
def main_page():
    print(f'Got a request from {request.remote_addr}')
    return f'Hello, {request.remote_addr}'


@app.route('/map', methods='GET')






@app.route('/plot')
def plot():
    print(f'Got a request from {request.remote_addr}')
    file_name = 'contrib_flask.svg'
    if not os.path.isfile(file_name):
        make_me()
    return send_from_directory('./', 'contrib_flask.svg')


if __name__ == '__main__':
    if socket.gethostname() == 'Marcos-Mac-Pro.local':
        app.run()
    else:
        app.run(debug=True, host='127.0.0.1', port=80)