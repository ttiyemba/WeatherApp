#!/usr/bin/env python3


from flask import Flask,flash,redirect,render_template,request,url_for
from pprint import pprint as pp
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(        'weather.html',        data=[{'name':'Reading'}, {'name':'Leicester'}, {'name':'Manchester'},        {'name':'Liverpool'}, {'name':'Leeds'}, {'name':'Bradford'},        {'name':'Coventry'}, {'name':'Sheffield'}, {'name':'Wolverhampton'},         {'name':'Sunderland'}])

@app.route('/result', methods=['GET','POST'])
def result():
     data = []    
     error = None    
     select = request.form.get('comp_select')
     resp = query_api(select)
     pp(resp)    
     if resp:
        data.append(resp)    
        if len(data) != 2:
            error = 'Bad Response from Weather API' 
     return render_template(        'result.html',        data=data,        error=error)


if __name__=='__main__':
    app.run(debug=True)