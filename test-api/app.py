import json
from flask import Flask, jsonify, request
import requests
app = Flask(__name__)


@app.route('/currency/euro/cad/<float:euro>')
def currency_conversion(euro):

    response = requests.get("http://data.fixer.io/api/latest?access_key=ACCESS_KEY&symbols=USD,CAD").content
    data = json.loads(response)
    rates = data["rates"]
    msg_str = "message: We have received CAD:"
    cad = rates['CAD'] * euro
    return jsonify({msg_str: cad})

if __name__ == "__main__":
    app.run(port=5000)

    
