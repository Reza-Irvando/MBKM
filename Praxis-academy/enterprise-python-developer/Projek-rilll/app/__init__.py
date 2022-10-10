from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})

from app import routes