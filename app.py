from flask import Flask, render_template, jsonify
from num_generator import Num_Generator
from db import Database
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)
database = Database()
num_generator = Num_Generator(database)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    #This picks a random number and returns it in json format
    num_generator.get_random_number()
    data = database.get_table_from_db()
    print(data)
    return jsonify(data[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)