import requests
from flask import Flask, render_template,jsonify
import json
import os
import config

app=Flask(__name__,template_folder='templates')
url = "https://api.apilayer.com/exchangerates_data/latest?symbols=INR%2CGBP%2CEUR%2CJPY%2CCNY%2CAUD%2CCAD&base=USD"

payload = {}

@app.route('/')
def home():
    response = requests.request("GET", url, headers=config.headers, data = payload)

    status_code = response.status_code
    result = response.text
    cur=json.loads(result)
    print(cur)
    
    #return cur['symbols']
    return render_template('index.html',currency=cur)

if __name__ == "__main__":
    app.run(debug=True)