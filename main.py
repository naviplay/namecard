# -*- coding: utf-8 -*-
from datetime import datetime
import os

from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return """<h1>Ralla namecard</h1>
    <img src="static/profile.jpeg" width="200" ></br></br>
    안녕하세요. 랄라입니다. </br>
    지금 시각은 """ + now() + """입니다."""


def now():
	return datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분')


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)