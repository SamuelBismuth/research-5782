import numpy as np
from flask import Flask, request, abort

from steinitz import steinitz_ip


app = Flask(__name__)


@app.route('/')
def index():
    return abort(404)


@app.route('/run_algorithm/', methods=["POST"])
def run_algorithm():
    data = request.get_json()
    print(data)
    A = np.array(data['A'])
    b = np.array(data['b'][0])
    c = np.array(data['c'][0])
    try:
        answer = steinitz_ip(c, A, b)
    except Exception as error:
        answer = 'error: ' + str(error)
    return answer


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)