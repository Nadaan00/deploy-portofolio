import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template
# from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# client = MongoClient('mongodb+srv://???:sparta@cluster0.gaybq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)