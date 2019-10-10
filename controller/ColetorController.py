from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
app = Flask (__name__)

@app.route("/paginaHTML")
def paginaHTML ():
    url = "http://journals.ecs.soton.ac.uk/java/tutorial/networking/urls/readingWriting.html"
    requisicao = requests.get (url)
    print ("Código HTTP de resposta: " + str (requisicao.status_code))
    pagina = requisicao.text
    return pagina

@app.route("/paginaTXT")
def paginaTXT ():
    url = "http://journals.ecs.soton.ac.uk/java/tutorial/networking/urls/readingWriting.html"
    requisicao = requests.get (url)
    print ("Código HTTP de resposta: " + str (requisicao.status_code))
    pagina = requisicao.text
    soup = BeautifulSoup (pagina)
    txt = soup.get_text ()
    return txt

if __name__ == "__main__":
    app.run ()