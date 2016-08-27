# -*- coding: utf-8 -*-
import test
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕하세요. 노란입니다."

@app.route("/job")
def job():
    return "카카오에 다닙니다."

if __name__ == "__main__":
    app.run()
