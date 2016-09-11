# -*- coding: utf-8 -*-
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕하세요. 랄라입니다. 반가워요. "

@app.route("/job")
def job():
    return "회사에 다닙니다."

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)