from flask import Flask
import requests

app = Flask(__name__)

@app.route('/dadjoke')
def dad():
    resp = requests.get('https://icanhazdadjoke.com/', headers={'Accept':'text/plain'})

    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    if  resp.status_code == 200:
        theJoke = resp.content.decode("utf-8")
    return theJoke

@app.route('/advice')
def advice():
    resp = requests.get('http://api.adviceslip.com/advice', headers={'Accept':'application/json'})

    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    if  resp.status_code == 200:
        theJoke = resp.content
    return theJoke

if __name__ == '__main__':
    app.run(host='0.0.0.0')