import flask
import json
from flask import request

import save_files

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route('/create', methods=['POST'])
def create_api():
    filename = request.args.get('filename')
    res = save_files.create_file(filename)
    return json.dumps(res, indent=4)

@app.route('/update', methods=['PUT'])
def update_api():
    filename = request.args.get('filename')
    content = request.args.get('content')
    res = save_files.change_file_content(filename, content)
    return json.dumps(res, indent=4)

@app.route('/read', methods=['GET'])
def read_api():
    filename = request.args.get('filename')
    res = save_files.read_file(filename)
    return json.dumps(res, indent=4)


app.run(debug=True, host='0.0.0.0', port=5000)
