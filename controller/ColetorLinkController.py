from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
app = Flask (__name__)

@app.route ("/coletar-link", methods=['POST']) 
def coletar_link (): 
    return jsonify ({"resp": "Coletor de link iniciado através do método POST."})
    