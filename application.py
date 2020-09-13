# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for,request,make_response
import RecipeAnalyzer

analyzer = RecipeAnalyzer.RecipeAnalyzer()

application = app = Flask(__name__)

@app.route('/matkol', methods = ['POST','GET'])
def getFoodprint():
    recipe = request.get_json(force=True)
    value  = analyzer.calculate(recipe)
    if(value>1000):
        return "Please don't"
    else:
        return str(value)+"kg"

@app.route('/')
def index():
    return render_template('interface.html')

if __name__=='__main__':
    application.run()
