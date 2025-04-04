from flask import Flask, render_template, jsonify
from num_generator import Num_Generator
import json

app = Flask(__name__)
num_generator = Num_Generator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    #This picks a random number and returns it in json format
    num_generator.get_random_number()
    with open('database.json', 'r') as file:
        data = json.load(file)
        
    return jsonify({"count": data["count"], "number": data["number"]})


if __name__ == '__main__':
    app.run(debug=True)