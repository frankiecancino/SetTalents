from flask import Flask, render_template, request
from SetTalents.app.subscribe import Subscriptions


app = Flask(__name__, static_url_path='')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        Subscriptions().store_email(email)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()