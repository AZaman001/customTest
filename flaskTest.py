import os
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/dadjoke')
def root():
    resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept':'text/plain'})

    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    if  resp.status_code == 200:
        theJoke = resp.content.decode("utf-8")
    return theJoke

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)